The [iPhone 6s specs](https://support.apple.com/kb/sp726?locale=en_US)
say it can record 720p video at 240 fps and 1080p video at 120 fps.  A
friend tells me he bought a replacement camera for US$8, including the
flex cable, but it was the front camera, which [is only 60fps for
720p](https://stackoverflow.com/questions/50082391/what-are-the-fps-of-the-facetime-camera-for-the-iphone-6s-vs-7-vs-x-vs-ipad-pro).

iPhone cameras are well-known for their rolling-shutter feature, where
they scan each line of the image out at a separate time during the
frame, leading to visual distortions of rapidly moving objects rather
than blur, at least when light is adequate.  So rather than
considering the back camera as a 240fps camera, it may be reasonable
to consider it as a 172800-line-per-second camera, although the gating
time (shutter speed) for each line might actually be longer than the
5.8 μs suggested there.  [Robert Elder reports success recording 660
frames per second][0] on a US$6 Raspberry Pi camera and 1007 frames
per second on the V2 camera by reading out the same lines over and
over again (so you get a smaller frame at a higher frame rate) but
alternatives include using a glass rod to defocus the camera in Y so
that every line sees almost exactly the same image, or to use two
parallel mirrors to kaleidoscopically replicate a small fraction of
the field of view several times.

[0]: https://blog.robertelder.org/recording-660-fps-on-raspberry-pi-camera/

Streak cameras are an extremely important research tool for
investigating all kinds of ultrafast phenomena, such as the time
evolution of an arc in air.
