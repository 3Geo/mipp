#
# $Id$
#

#-----------------------------------------------------------------------------
#
# All exception from the mipp module
#
#-----------------------------------------------------------------------------
class MippError(Exception):
    pass

#-----------------------------------------------------------------------------
#
# Decoding error
#
#-----------------------------------------------------------------------------
class DecondingError(MippError):
    pass
class UnknownSatellite(MippError):
    pass
#-----------------------------------------------------------------------------
#
# Image readings error
#
#-----------------------------------------------------------------------------
class ReaderError(MippError):
    pass

class NoFiles(ReaderError):
    pass

#-----------------------------------------------------------------------------
#
# Config file reader error
#
#-----------------------------------------------------------------------------
class ConfigReaderError(MippError):
    pass

#-----------------------------------------------------------------------------
#
# Navigations error
#
#-----------------------------------------------------------------------------
class NavigationError(MippError):
    pass

#-----------------------------------------------------------------------------
#
# Calibrations error
#
#-----------------------------------------------------------------------------
class CalibrationError(MippError):
    pass
