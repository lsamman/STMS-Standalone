import math
"""Storage depot numbers, KSP metres; z = 0 at the joint's stack node on SEP's Block 3 core."""
import hls_layout as HL
STRETCH = 7.6                # the chart's depot stands 1.23 times as tall as the tanker beside it
ZB = HL.Z_SKIN - HL.Z_TOP; ZJ = HL.Z_OGIVE - HL.Z_TOP + STRETCH; RING = 1.1427      # skin's lower edge; barrel-ogive joint; ring height (SEP's weld spacing)
C, R0, ZE = 16.75, 2.80, ZJ - .75                          # raceway: centre azimuth, hull radius, top
SEC = [(C + 4.6 * math.cos(math.pi * k / 12), R0 + .005 + .24 * math.sin(math.pi * k / 12)) for k in range(13)]      # section: a half ellipse, azimuth and radius
RINGS = [(0, 1, 1)] + [(.55 * math.sin(math.radians(a)), .35 + .65 * math.cos(math.radians(a)), max(.02, math.cos(math.radians(a)))) for a in (15, 30, 45, 60, 75, 85, 90)]      # domed end
UNITS = 50000                # about 330 m3, at the density of SEP's own tanks less room for coolers and ends
