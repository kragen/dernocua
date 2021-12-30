Trying to get a PS/2 keyboard to work with an Arduino Duemilanove.

Notes on the PS/2 keyboard protocol
-----------------------------------

[Adam Chapweske’s physical-layer
guide](http://www.burtonsys.com/ps2_chapweske.htm) clarifies the key
points:

> I use a few tricks when implementing an open-collector interface
> with PIC microcontrollers.  I use the same pin for both input and
> output, and I enable the PIC’s internal pullup resistors rather than
> using external resistors.  A line is pulled to ground by setting the
> corresponding pin to output, and writing a “zero” to that port.  The
> line is set to the “high impedance” state by setting the pin to
> input.  Taking into account the PIC’s built-in protection diodes and
> sufficient current sinking, I think this is a valid configuration.
> Let me know if your experiences have proved otherwise. ...
> 
> The PS/2 mouse and keyboard implement a bidirectional synchronous
> serial protocol.  The bus is “idle” when both lines are high
> (open-collector).  This is the only state where the keyboard/mouse
> is allowed begin transmitting data.  The host has ultimate control
> over the bus and may inhibit communication at any time by pulling
> the Clock line low.

The PIC approach should work the same with AVRs, I think.

> The device always generates the clock signal.  If the host wants to
> send data, it must first inhibit communication from the device by
> pulling Clock low.  The host then pulls Data low and releases Clock.
> This is the “Request-to-Send” state and signals the device to start
> generating clock pulses.
> 
> Data sent from the device to the host is read on the falling edge of
> the clock signal; data sent from the host to the device is read on
> the rising edge.  The clock frequency must be in the range
> 10-16.7kHz.  This means clock must be high for 30-50 microseconds
> and low for 30-50 microseconds.  If you’re designing a keyboard,
> mouse, or host emulator, you should modify/sample the Data line in
> the middle of each cell, i.e., 15-25 microseconds after the
> appropriate clock transition.

At the Duemilanove’s 16 MHz, 15-25 microseconds is 240-400 clock
cycles, so we can probably get by with polling rather than interrupts,
at least initially.

[Chapweske also wrote a guide to the logical
protocol](https://web.archive.org/web/20050315093045/panda.cs.ndsu.nodak.edu/~achapwes/PICmicro/keyboard/atkeyboard.html).

Existing Arduino software is worth trying but will be insufficient
------------------------------------------------------------------

[There’s an LGPL-licensed library called
PS2Keyboard](https://www.pjrc.com/teensy/td_libs_PS2Keyboard.html),
last updated [2 years
ago](https://github.com/PaulStoffregen/PS2Keyboard), with the last
release 5 years ago, for speaking this protocol; its interface looks
very simple.  [The page on arduino.cc is even more out of
date](https://playground.arduino.cc/Main/PS2Keyboard/), which I guess
makes sense since it’s been read-only since 02018.

    keyboard.begin(DataPin, IRQpin); ...
    if (keyboard.available()) {
      char c = keyboard.read();
      if (c == PS2_ENTER) {
        Serial.println(); ...
      } else {
        Serial.print(c);
      }

However, this interface has a couple of major drawbacks:

- It doesn’t provide key-release data.
- Multiple special keys like F1 and F2 are all mapped to the same
  character code.  (There’s a `get_scan_code` function but it’s
  `static`.)

The implementation also has a couple of drawbacks:

- It uses 52 bytes of RAM for buffering the keys.
- It uses an interrupt --- though this is probably unavoidable with
  any decent interface.
- It always puts three separate 409-byte keymaps in ROM (US-English,
  French, German).
- It doesn’t provide any of the messages *to* the keyboard, such as
  pinging it (“echo”, 0xee), setting the scan code set (0xf0), and,
  most importantly, setting the keyboard LEDs (0xed).

Buffering on the keyboard?
--------------------------

[The Wikipedia page has an intriguing comment suggesting a
fully-polled mode of
operation](https://en.wikipedia.org/wiki/PS/2_port):

> When the host pulls Clock low, the device must immediately stop
> transmitting and release Clock and Data to both float high. ... The
> host can use this state of the interface simply to inhibit the
> device from transmitting when the host is not ready to receive. (For
> the IBM PC keyboard port, this was the only normal use of signalling
> from the computer to the keyboard. The keyboard could not be
> commanded to retransmit a keyboard scan code after it had been sent,
> since there was no reverse data channel to carry commands to the
> keyboard, so the only way to avoid losing scan codes when the
> computer was too busy to receive them was to inhibit the keyboard
> from sending them until the computer was ready. This mode of
> operation is still an option on the IBM AT and PS/2 keyboard port.)

This suggests the possibility that you could pull the clock line low
all the time except when polling for a keystroke, trusting the
keyboard to buffer any keypresses, but I’d be surprised if that worked
reliably.  In any case, it would require waiting for the minimum
timeout to see if the keyboard was going to send anything...

Experiment notes
----------------

I have an Arduino Duemilanove here.  It can successfully run the Blink
and ASCIITable examples, so it’s at least mostly working.

The keyboard is an IBM KB-9910, Latin American layout with Windows
key, which seems on first glance to be in pretty good shape aside from
being dusty.  The main board is a single-sided board built around a
large Chicony DIP, 40 pins I think, with lots of through-hole parts.
The keyboard switch silicone domes are all molded from a single
silicone sheet, which fortunately means they can’t get lost
individually.  The main board is connected to the
thoroughly-strain-relieved cable with a four-pin Dupont connector,
with four lines on the board labeled G (violet), V (brown), D (red),
and C (yellow); presumably these are ground, Vcc, data, and clock.

I reassembled the keyboard, cut off the PS/2 connector, stripped the
cable a bit, and soldered pins individually to the wires.  Plugging
the brown and violet wires into the 5V and GND pins on the Duemilanove
doesn’t seem to harm the Duemilanove, which has its pin-13 LED
blinking happily.

The next step, I think, is to measure sequences of data transitions
and send them over the Arduino’s serial port.  There’s an [Arduino
sketch under a 2-clause BSD license by Andrew Gillham that implements
the SUMP logic analyzer protocol and something called Openbench Logic
Sniffer](https://sigrok.org/wiki/Arduino) at 4 MHz, with [triggering
support and stuff](https://github.com/gillham/logic_analyzer).  This
might allow sigrok to use the Arduino to view these signals without
needing to write more code.  And, to my surprise, sigrok already has
[a PS/2 protocol decoder in
it](https://www.sigrok.org/blog/new-protocol-decoder-ps2)!  So if I
can just get some signal data into pulseview, I can see what data the
keyboard is sending.

I burned the sketch to the Arduino and connected to it in Pulseview:
“Choose the driver: Openbench Logic Sniffer & SUMP compatibles (ols);
Choose the interface: /dev/ttyUSB2 (FT232R USB UART - A6008ePZ); Scan
for devices using driver above [usually twice]; Select the device:
AGLAv0 with 6 channels.”  I’m trying to do captures at 200 kHz.

(Mark R. Rubin has also written a [somewhat more powerful GPL firmware
for the Blue
Pill](https://www.cnx-software.com/2020/11/14/turn-1-5-blue-pill-stm32-board-into-a-sigrok-compatible-logic-analyzer/)
called “buck50” that can do [6 Msps, 5k samples, and 8
channels](https://github.com/thanks4opensource/buck50), and also a 1
MHz analog oscilloscope.  (Too bad my Blue Pill is at home.)  But it
doesn’t seem to work directly with sigrok; he suggests using Gnuplot
to plot CSV files, saying sigrok uses too much RAM.)

Okay, I haven’t figured out how to set up triggering, and the sample
buffer is only 5 milliseconds long, but by doing a lot of key repeat
and capturing over and over again, I think I got it to capture a
keystroke.  (This happens about one out of every 32-64 tries.)  It
does show a nice 10.0 kHz clock on the yellow wire and some kind of
data on the red wire.  The whole packet is 1.020 ms long, with 10
positive clock pulses (and 11 low states) in 1.050 ms.  This means 11
falling clock transitions, which seems to be correct.

I get about 9 samples during each clock pulse.  Sigrok’s PS/2 protocol
decoder is silent about what any of this means.

Oh, now [I’ve told it to trigger on the clock going low, by clicking
on the little “0” tag in the left
margin](https://sigrok.org/doc/pulseview/0.4.1/manual.html#_triggers).
I was thinking that it was triggering too late because the data packet
is at the very end of the window, but actually I think this is a bug
people have reported in the past in the Arduino sketch: the values are
time-reversed.  So the triggering packet is at the very end of the
window instead of the beginning, and it’s backwards so the PS/2
protocol decoder can’t decode it.  Also, after the first triggering,
if I do a second capture it never runs again unless I reset the
Arduino.

Setting the sample speed down to 50 kHz gives me a 20.5 millisecond
window instead of a 5 millisecond window; 20 kHz is too slow and
misses some clock cycles.  With this I was finally able to see the
two-byte sequence that indicates a key-release event; there are 3.92
ms from the start of one byte to the start of the other, so the whole
sequence takes 4.94 ms.

A capture at “5 MHz” has 5 full clock cycles in 0.3765 ms, 75.3 us per
bit, which is really more like 13000 bits persecond.  The whole
1024-sample buffer is some 511 us long, and the samples are evidently
two per microsecond, so I guess it’s sampling at 2 MHz.

I tweaked the sketch to send back the samples in reverse order from
how they were being sent:

	  /*
	   * dump the samples back to the SUMP client.  nothing special
	   * is done for any triggers, this is effectively the 0/100 buffer split.
	   */
	  for (i = 0 ; i < readCount; i++) {
	#ifdef USE_PORTD
		Serial.write(logicdata[readCount - i - 1] >> 2);
	#else
		Serial.write(logicdata[readCount - i - 1]);
	#endif
	  }

This does not seem to have made any difference, but I think I maybe
made the change in the wrong place.  This was the right place:

		if (trigger) {
		  while ((trigger_values ^ CHANPIN) & trigger);
		}

		for (i = 0 ; i < readCount; i++) {
		  logicdata[i] = CHANPIN;
		  delay(delayTime);
		}
	  }
	  for (i = 0 ; i < readCount; i++) {
	#ifdef USE_PORTD
		Serial.write(logicdata[readCount - i - 1] >> 2);
	#else
		Serial.write(logicdata[readCount - i - 1]);
	#endif

Now time flows forward, but sigrok’s PS/2 decoder is still not able to
decode the data.

However, I did manage to get something out of its SPI decoder.  At
first I was trying to decode the bits MSB-first, but that’s wrong;
they’re LSB-first.

Aha, finally I got the PS/2 decoder to decode the F0 of a key-release
event!  It apparently doesn’t decode the *last* byte in a capture (I
guess because it’s missing the falling clock transition that indicates
the end of the bit) and all of my captures are too short so far.

Now I’ve verified that pressing the “A” key produces [the correct 0x1C
scan
code](https://techdocs.altium.com/display/FPGA/PS2+Keyboard+Scan+Codes);
the SPI decoder set for clock polarity 1, clock phase 0, lsb-first bit
order, 11 bits decodes the sequence 00011100001: start bit 0, data
bits 0011 1000 (0x1C LSB-first), odd parity bit 0, stop bit 1.  The
SPI decoder renders this as “438” in hex, which is just shifted left
by 1 bit (the start bit):

	>>> hex(0x438 >> 1)
	‘0x21c’

Left shift gives “624”, 00100100011, which should be scan code 0x12.
This seems to be correct.  And sometimes I instead get 0xF0 0x12,
which is the correct key release code.

I feel like for such slow signals it ought to be possible to send a
continuous stream of bytes over the Arduino’s serial port.

So, at least I understand the PS/2 signals, and the keyboard seems to
work properly.
