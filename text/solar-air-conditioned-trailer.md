I was watching [Adam Booth’s video on the 3 kW generator he runs his
travel trailer’s air conditioner from][0], and I realized there was a
connection between solar-panel efficiency and insulation thickness.

[0]: https://youtu.be/ciJX6eVLuH0

Straw bales conduct about 0.5 W/m/K of heat; modern insulation
materials like polyisocyanurate foam are closer to 0.2, and IIRC
firebrick is closer to 0.8.  Mainstream solar panels are about 21%
efficient, the solar constant is nominally 1000 W/m², and commonplace
air-source air conditioners and similar heat pumps have a coefficient
of performance (for cooling) of about 2, so they pump out about 2 W of
heat for every W of electrical power they consume.

Suppose you have a dwelling pod that’s perfectly insulated on every
side, except that one side is covered in solar panels and has sunlight
falling on it.  The sun heats up the solar panels to 50°, even if the
outdoor air is a little cooler, but the interior needs to stay below
24° to remain habitable.  How thick does the insulation need to be for
the air conditioner (hypothetically not blocking any sun) to keep up
with the heat leakage through the insulation?

Well, you’re getting 1000 W/m² of sunlight and 210 W/m² of electrical
power, which provides you with 420 W/m² of cooling.  The heat delta
from the solar panel to the cool interior is 26° (26 K), so straw
insulation has 13 W/m flowing through it, which is to say, 13 W m/m².
Multiplying 420 W/m² by 31 mm of straw gives you those 13 W/m.  As
little as 12 mm of styrofoam might be enough.

If your pod has four times as much area exposed to the hot outdoors as
to the hot solar panel, like a travel trailer might, the insulation
needs to be four times as thick, like 150 mm of straw or 50 mm of
styrofoam.  This is still eminently feasible.

Aside from heat leakage by conduction through the walls, every square
meter of sunlight you let in through a window adds 1000 W of heating
during the day; removing that requires just over 2 m² of solar panels
to power the air conditioner.

Normally when you’re calculating the energy output of solar panels you
need to take the capacity factor into account, which may vary from as
little as 10% in polar countries like Germany or the UK to more than
30% in very sunny places (California’s about 29%), but, in this case,
when the sun isn’t shining to power the air conditioner, it also isn’t
heating up your roof and walls.

Possibly desiccant-based air conditioning systems are a better fit for
solar energy, since they can directly use the heat from the sunlight,
but nowadays PV panels are amazingly cheap even compared to solar
thermal collectors.
