#
# - Fill a mda Metadata object with meta data
# - Fill a numpy array with image data
# 
# Return:
#    meta-data, image-data
#
import sys
import mda
from bin_reader import *
from array_reader import *
import numpy as np
from avhrr_data import *
from datetime import datetime

RECORD_LENGTH = 2048
CHANNEL_COUNT = 5
BAD_RECORD_FLAG = pow(2, 31)

md = mda.Metadata()

l1b_file = sys.argv[1]
fp = open(l1b_file, 'rb')

# General information
md.siteid = fp.read(3)
md.blank = fp.read(1)
md.l1bversnb = read_uint2(fp.read(2))
md.l1bversyr = read_uint2(fp.read(2))
md.l1bversdy  = read_uint2(fp.read(2))
md.reclg = read_uint2(fp.read(2))
md.blksz = read_uint2(fp.read(2))
md.hdrcnt = read_uint2(fp.read(2))
# filler0
fp.read(6)
md.dataname = fp.read(42)

md.prblkid = fp.read(8)
md.satid = read_uint2(fp.read(2))
md.instid = read_uint2(fp.read(2))
md.datatyp = read_uint2(fp.read(2))

md.tipsrc = read_uint2((fp.read(2)))
md.startdatajd = read_uint4(fp.read(4))
md.startdatayr = read_uint2(fp.read(2))
md.startdatady = read_uint2(fp.read(2))
md.startdatatime = read_uint4(fp.read(4))
md.start_datetime = (datetime(md.startdatayr, 1, 1) +
                     timedelta(days = md.startdatady - 1) +
                     timedelta(milliseconds = md.startdatatime))                             

md.enddatajd = read_uint4(fp.read(4))
md.enddatayr = read_uint2(fp.read(2))
md.enddatady = read_uint2(fp.read(2))
md.enddatatime = read_uint4(fp.read(4))
md.end_datetime = (datetime(md.enddatayr, 1, 1) +
                   timedelta(days = md.enddatady - 1) +
                   timedelta(milliseconds = md.enddatatime))                             

md.cpidsyr = read_uint2(fp.read(2))
md.cpidsdy = read_uint2(fp.read(2))
# filler1
fp.read(8)

# Data set quality indicators
md.inststat1 = read_uint4(fp.read(4))
# filler2
fp.read(2)

md.statchrecnb = read_uint2(fp.read(2))
md.inststat2 = read_uint4(fp.read(4))
md.scnlin = read_uint2(fp.read(2))
md.callocscnlin = read_uint2(fp.read(2))
md.misscnlin = read_uint2(fp.read(2))
md.datagaps = read_uint2(fp.read(2))

md.okdatafr = read_uint2(fp.read(2))
md.pacsparityerr = read_uint2(fp.read(2))
md.auxsyncerrsum = read_uint2(fp.read(2))
md.timeseqerr = read_uint2(fp.read(2))
md.timeseqerrcode = read_uint2(fp.read(2))
md.socclockupind = read_uint2(fp.read(2))
md.locerrind = read_uint2(fp.read(2))
md.locerrcode = read_uint2(fp.read(2))
md.pacsstatfield = read_uint2(fp.read(2))
md.pacsdatasrc = read_uint2(fp.read(2))

# filler3
fp.read(4)
md.spare1 = fp.read(8)
md.spare2 = fp.read(8)
# filler4
fp.read(10)


# Calibration

md.racalind = read_uint2(fp.read(2)) 
md.solarcalyr = read_uint2(fp.read(2))
md.solarcaldy = read_uint2(fp.read(2))
md.pcalalgind = read_uint2(fp.read(2))
md.pcalalgopt = read_uint2(fp.read(2))
md.scalalgind = read_uint2(fp.read(2))
md.scalalgopt = read_uint2(fp.read(2))

md.irttcoef = np.empty((4,6),int)
for i in range(4):
    for j in range(6):
        md.irttcoef[i][j] = read_int2(fp.read(2))
   
# filler5
fp.read(8)

# Radiance to temperature conversion

md.albcnv = np.empty((2,3),int)
for i in range(2):
    for j in range(3):
        md.albcnv[i][j] = read_int4(fp.read(4))

md.radtempcnv = np.empty((3,3),int)
for i in range(3):
    for j in range(3):
        md.radtempcnv[i][j] = read_int4(fp.read(4))

# filler6
fp.read(12)

# Navigation
md.modelid = fp.read(8) 
md.nadloctol = read_uint2(fp.read(2))
md.locbit = read_uint2(fp.read(2))
# filler7
fp.read(2)
md.rollerr = read_uint2(fp.read(2))
md.pitcherr = read_uint2(fp.read(2))
md.yawerr = read_uint2(fp.read(2))
md.epoyr = read_uint2(fp.read(2))
md.epody = read_uint2(fp.read(2))
md.epotime = read_uint4(fp.read(4))
md.smaxis = read_uint4(fp.read(4))
md.eccen = read_uint4(fp.read(4))
md.incli = read_uint4(fp.read(4))
md.argper = read_uint4(fp.read(4))
md.rascnod = read_uint4(fp.read(4))
md.manom = read_uint4(fp.read(4))
md.xpos = read_int4(fp.read(4))
md.ypos = read_int4(fp.read(4))
md.zpos = read_int4(fp.read(4))
md.xvel = read_int4(fp.read(4))
md.yvel = read_int4(fp.read(4))
md.zvel = read_int4(fp.read(4))
md.earthsun = read_uint4(fp.read(4))
# filler8
fp.read(16)

# Analog Telemetry conversion

md.pchtemp = read_intarray(fp, 5)
md.reserved1 = read_int2(fp.read(2))

md.pchtempext = read_intarray(fp, 5)  
md.reserved2 = read_int2(fp.read(2))
    
md.pchpow = read_intarray(fp, 5)
md.reserved3 = read_int2(fp.read(2))

md.rdtemp = read_intarray(fp, 5)
md.reserved4 = read_int2(fp.read(2))

md.bbtemp1 = read_intarray(fp, 5)
md.reserved5 = read_int2(fp.read(2))

md.bbtemp2 = read_intarray(fp, 5)
md.reserved6 = read_int2(fp.read(2))

md.bbtemp3 = read_intarray(fp, 5)
md.reserved7 = read_int2(fp.read(2))

md.bbtemp4 = read_intarray(fp, 5)
md.reserved8 = read_int2(fp.read(2))

md.eleccur = read_intarray(fp,5)
md.reserved9 = read_int2(fp.read(2))

md.motorcur = read_intarray(fp, 5)
md.reserved10 = read_int2(fp.read(2))

md.earthpos = read_intarray(fp, 5)
md.reserved11 = read_int2(fp.read(2))

md.electemp = read_intarray(fp, 5)
md.reserved12 = read_int2(fp.read(2))

md.chtemp = read_intarray(fp, 5)
md.reserved13 = read_int2(fp.read(2))

md.bptemp = read_intarray(fp, 5)
md.reserved14 = read_int2(fp.read(2))

md.mhtemp = read_intarray(fp, 5)
md.reserved15 = read_int2(fp.read(2))

md.adcontemp = read_intarray(fp, 5)
md.reserved16 = read_int2(fp.read(2))

md.d4bvolt = read_intarray(fp, 5)
md.reserved17 = read_int2(fp.read(2))

md.d5bvolt = read_intarray(fp, 5)
md.reserved18 = read_int2(fp.read(2))

md.bbtempchn3B = read_intarray(fp, 5)
md.reserved19 = read_int2(fp.read(2))

md.bbtempchn4 = read_intarray(fp, 5)
md.reserved20 = read_int2(fp.read(2))

md.bbtempchn5 = read_intarray(fp, 5)
md.reserved21 = read_int2(fp.read(2))

md.refvolt = read_intarray(fp, 5)
md.reserved22 = read_int2(fp.read(2))

# filler9
fp.read(2*10664)

print md

# Each element maps to one channel
scanline_count = md.scnlin
md.datarecord = np.empty(scanline_count, type(object))

print "number of scnlines: ", scanline_count
# One data record for one AVHRR scan line
for i in range(scanline_count):
	metadata = AvhMetadata()
        metadata.scnlin = read_int2(fp.read(2))
	metadata.scnlinyr = read_int2(fp.read(2))
	metadata.scnlindy = read_int2(fp.read(2))
	metadata.clockdrift = read_int2(fp.read(2))
	metadata.scnlintime = read_int4(fp.read(4))
	metadata.scnlinbit = read_int2(fp.read(2))

        metadata.datetime = (datetime(metadata.scnlinyr, 1, 1) +
                             timedelta(days = metadata.scnlindy - 1) +
                             timedelta(milliseconds = metadata.scnlintime))                             

        # filler
	fp.read(10)
	# Quality indicators
	metadata.qualind = read_int4(fp.read(4))
	metadata.scnlinqual = read_int4(fp.read(4))
	metadata.calqual = read_intarray(fp, 3)
	metadata.cbiterr = read_int2(fp.read(2))
        # filler
	fp.read(8)
	# Calibration coefficients
	metadata.calvis = read_int4array3(fp, 5, 3, 3)
	metadata.calir = read_int4array3(fp, 3, 2, 3)
	print "\nscnlin:", metadata.scnlin
        if (metadata.qualind & BAD_RECORD_FLAG):
            print "    BAD RECORD"
        else:
            print "    scnlinyr:", metadata.scnlinyr
            print "    scnlindy:", metadata.scnlindy
            print "    clockdrift:", metadata.clockdrift
            print "    scnlintime:", metadata.scnlintime
            print "    datetime:", metadata.datetime
            print "    scnlinbit: 0x%02x"%metadata.scnlinbit
            print "    qualind: 0x%08x"%metadata.qualind
            print "    scnlinqual: 0x%08x"%metadata.scnlinqual
            print "    calqual:",
            for i in metadata.calqual:
                print " 0x%02x"%i,
            print ''
            print "    cbiterr:", metadata.cbiterr
            print "    calvis:\n", metadata.calvis
            print "    calir:\n", metadata.calir
        # filler
	fp.read(12)

	# Navigation
	metadata.navstat = read_int4(fp.read(4))
	metadata.attangtime = read_int4(fp.read(4))
	metadata.rollang = read_int2(fp.read(2))
	metadata.pitchang = read_int2(fp.read(2))
	metadata.yawang = read_int2(fp.read(2))
	metadata.scalti = read_int2(fp.read(2))
	metadata.ang = read_int2array2(fp, 3, 51)
        # filler
	fp.read(6)
	metadata.pos = read_int4array2(fp, 2, 51)
        # filler
	fp.read(8)

	# HRPT minor frame telemetry
	metadata.telem = read_intarray(fp, 103)
        # filler
	fp.read(2)

	# AVHRR sensor data
	databuffer = fp.read(RECORD_LENGTH*2*CHANNEL_COUNT)
	scnline_data = np.frombuffer(databuffer, dtype = 'int16', count = RECORD_LENGTH * CHANNEL_COUNT)
	interleaved_data = scnline_data.reshape(RECORD_LENGTH, CHANNEL_COUNT)
	channel_data = np.rollaxis(interleaved_data, 1, 0)
        """        
	print 'scnlin:', metadata.scnlin,"[0][0]:", channel_data[0][0]
	print 'scnlin:', metadata.scnlin,"[0][1]:", channel_data[0][1]
        print '\n'
        """
        # filler
	fp.read(8)

	# Tip minor frame header
	metadata.tipmfhd = read_int2array2(fp, 7, 5)
	metadata.cputel = read_chararray2(fp, 2, 5)
	metadata.icputel = read_int2array2(fp, 6, 5)
        # filler
	fp.read(2*37)
	
	md.datarecord[i] = AvhDataRecord(channel_data, metadata)

# Result
# General header md
# Including records AvhDataRecord->data, AvhDataRecord->meta_data
# for each data record [chn][2048]
#
# md
# def calibrate(datarecord), where the output is
# (data[scnlin][2048], data[scnlin][2048], data[scnlin][2048], data[scnlin][2048], data[scnlin][2048])
#
record = md.datarecord[0]
for c in range(CHANNEL_COUNT):
    print record.data[c]

"""
keyfile = open('old_md_order', 'rb')
oldkey = []
for line in keyfile.readlines():
    oldkey = line.strip('\n')
    print oldkey, ' = ', getattr(md, oldkey)
"""
