#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 SMHI

# Author(s):

#   Martin Raspaud <martin.raspaud@smhi.se>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Reader for aapp level 1b data.

http://research.metoffice.gov.uk/research/interproj/nwpsaf/aapp/NWPSAF-MF-UD-003_Formats.pdf
"""


filename = "/local_disk/data/satellite/polar/noaa19_20100224_1129_05402/hrpt_noaa19_20100224_1129_05402.l1b"

import numpy as np

# AAPP 1b header

headertype = np.dtype([("siteid", "S3"),
                       ("blank", "S1"),
                       ("l1bversnb", "<u2"),
                       ("l1bversyr", "<u2"),
                       ("l1bversdy", "<u2"),
                       ("reclg", "<u2"),
                       ("blksz", "<u2"),
                       ("hdrcnt", "<u2"),
                       ("filler0", "S6"),
                       ("dataname", "S42"),
                       ("prblkid", "S8"),
                       ("satid", "<u2"),
                       ("instid", "<u2"),
                       ("datatype", "<u2"),
                       ("tipsrc", "<u2"),
                       ("startdatajd", "<u4"),
                       ("startdatayr", "<u2"),
                       ("startdatady", "<u2"),
                       ("startdatatime", "<u4"),
                       ("enddatajd", "<u4"),
                       ("enddatayr", "<u2"),
                       ("enddatady", "<u2"),
                       ("enddatatime", "<u4"),
                       ("cpidsyr", "<u2"),
                       ("cpidsdy", "<u2"),
                       ("filler1", "S8"),
                       # data set quality indicators
                       ("inststat1", "<u4"),
                       ("filler2", "S2"),
                       ("statchrecnb", "<u2"),
                       ("inststat2", "<u4"),
                       ("scnlin", "<u2"),
                       ("callocscnlin", "<u2"),
                       ("misscnlin", "<u2"),
                       ("datagaps", "<u2"),
                       ("okdatafr", "<u2"),
                       ("pacsparityerr", "<u2"),
                       ("auxsyncerrsum", "<u2"),
                       ("timeseqerr", "<u2"),
                       ("timeseqerrcode", "<u2"),
                       ("socclockupind", "<u2"),
                       ("locerrind", "<u2"),
                       ("locerrcode", "<u2"),
                       ("pacsstatfield", "<u2"),
                       ("pacsdatasrc", "<u2"),
                       ("filler3", "S4"),
                       ("spare1", "S8"),
                       ("spare2", "S8"),
                       ("filler4", "S10"),
                       # Calibration
                       ("racalind", "<u2"),
                       ("solarcalyr", "<u2"),
                       ("solarcaldy", "<u2"),
                       ("pcalalgind", "<u2"),
                       ("pcalalgopt", "<u2"),
                       ("scalalgind", "<u2"),
                       ("scalalgopt", "<u2"),
                       ("irttcoef", "<u2", (4, 6)),
                       ("filler5", "<i4", (2, )),
                       # radiance to temperature conversion
                       ("albcnv", "<i4", (2, 3)),
                       ("radtempcnv", "<i4", (3, 3)),
                       ("filler6", "<i4", (3, )),
                       # Navigation
                       ("modelid", "S8"),
                       ("nadloctol", "<u2"),
                       ("locbit", "<u2"),
                       ("filler7", "S2"),
                       ("rollerr", "<u2"),
                       ("pitcherr", "<u2"),
                       ("yawerr", "<u2"),
                       ("epoyr", "<u2"),
                       ("epody", "<u2"),
                       ("epotime", "<u4"),
                       ("smaxis", "<u4"),
                       ("eccen", "<u4"),
                       ("incli", "<u4"),
                       ("argper", "<u4"),
                       ("rascnod", "<u4"),
                       ("manom", "<u4"),
                       ("xpos", "<i4"),
                       ("ypos", "<i4"),
                       ("zpos", "<i4"),
                       ("xvel", "<i4"),
                       ("yvel", "<i4"),
                       ("zvel", "<i4"),
                       ("earthsun", "<u4"),
                       ("filler8", "S16"),
                       # analog telemetry conversion
                       ("pchtemp", "<u2", (5, )),
                       ("reserved1", "<u2"),
                       ("pchtempext", "<u2", (5, )),
                       ("reserved2", "<u2"),
                       ("pchpow", "<u2", (5, )),
                       ("reserved3", "<u2"),
                       ("rdtemp", "<u2", (5, )),
                       ("reserved4", "<u2"),
                       ("bbtemp1", "<u2", (5, )),
                       ("reserved5", "<u2"),
                       ("bbtemp2", "<u2", (5, )),
                       ("reserved6", "<u2"),
                       ("bbtemp3", "<u2", (5, )),
                       ("reserved7", "<u2"),
                       ("bbtemp4", "<u2", (5, )),
                       ("reserved8", "<u2"),
                       ("eleccur", "<u2", (5, )),
                       ("reserved9", "<u2"),
                       ("motorcur", "<u2", (5, )),
                       ("reserved10", "<u2"),
                       ("earthpos", "<u2", (5, )),
                       ("reserved11", "<u2"),
                       ("electemp", "<u2", (5, )),
                       ("reserved12", "<u2"),
                       ("chtemp", "<u2", (5, )),
                       ("reserved13", "<u2"),
                       ("bptemp", "<u2", (5, )),
                       ("reserved14", "<u2"),
                       ("mhtemp", "<u2", (5, )),
                       ("reserved15", "<u2"),
                       ("adcontemp", "<u2", (5, )),
                       ("reserved16", "<u2"),
                       ("d4bvolt", "<u2", (5, )),
                       ("reserved17", "<u2"),
                       ("d5bvolt", "<u2", (5, )),
                       ("reserved18", "<u2"),
                       ("bbtempchn3B", "<u2", (5, )),
                       ("reserved19", "<u2"),
                       ("bbtempchn4", "<u2", (5, )),
                       ("reserved20", "<u2"),
                       ("bbtempchn5", "<u2", (5, )),
                       ("reserved21", "<u2"),
                       ("refvolt", "<u2", (5, )),
                       ("reserved22", "<u2"),
])

# AAPP 1b scanline

scantype = np.dtype([("scnlin", "<i2"),
                     ("scnlinyr", "<i2"),
                     ("scnlindy", "<i2"),
                     ("clockdrift", "<i2"),
                     ("scnlintime", "<i4"),
                     ("scnlinbit", "<i2"),
                     ("filler0", "S10"),
                     ("qualind", "<i4"),
                     ("scnlinqual", "<i4"),
                     ("calqual", "<u2", (3, )),
                     ("cbiterr", "<i2"),
                     ("filler1", "S8"),
                     # Calibration
                     ("calvis", "<i4", (3, 3, 5)),
                     ("calir", "<i4", (3, 2, 3)),
                     ("filler2", "<i4", (3, )),
                     ("navstat", "<i4"),
                     ("attangtime", "<i4"),
                     ("rollang", "<i2"),
                     ("pitchang", "<i2"),
                     ("yawang", "<i2"),
                     ("scalti", "<i2"),
                     ("ang", "<i2", (3, 51)),
                     ("filler3", "<i2", (3, )),
                     ("pos", "<i4", (51, 2)),
                     ("filler4", "<i4", (2, )),
                     ("telem", "<i2", (103, )),
                     ("filler5", "<i2"),
                     ("hrpt", "<i2", (2048, 5)),
                     ("filler6", "<i4", (2, )),
                     # tip minor frame header
                     ("tipmfhd", "<i2", (7, 5)),
                     # cpu telemetry
                     ("cputel", "S6", (2, 5)),
                     ("filler7", "<i2", (67, )),
                     ])
                     

def show(data):
    """Show the stetched data.
    """
    import Image as pil
    img = pil.fromarray(np.array((data - data.min()) * 255.0 /
                                 (data.max() - data.min()), np.uint8))
    img.show()

import datetime
tic = datetime.datetime.now()

with open(filename, "rb") as fp_:
    arr =  np.fromfile(fp_, dtype=headertype, count=1)
    fp_.seek(10664 * 2, 1)
    arr2 = np.fromfile(fp_, dtype=scantype)

print "reading time", datetime.datetime.now() - tic
#show(arr2["hrpt"][:, :, 0])


# visible calibration

# Calibration count to albedo, the calibration is performed separately for two
# value ranges.
channel = arr2["hrpt"][:, :, 0].astype(np.float)
mask1 = channel <= np.expand_dims(arr2["calvis"][:, 0, 2, 4], 1)
mask2 = channel > np.expand_dims(arr2["calvis"][:, 0, 2, 4], 1)

channel[mask1] = (channel * np.expand_dims(arr2["calvis"][:, 0, 2, 0] * 1e-10, 1) + np.expand_dims(arr2["calvis"][:, 0, 2, 1] * 1e-7, 1))[mask1]

channel[mask2] = (channel * np.expand_dims(arr2["calvis"][:, 0, 2, 2] * 1e-10, 1) + np.expand_dims(arr2["calvis"][:, 0, 2, 3] * 1e-7, 1))[mask2]

channel[channel<0] = 0
show(channel)
# ir calibration
# see /local_disk/usr/src/ahamap2/ahamap-pps-2010-patches/src/pymodules/avhrr.c
