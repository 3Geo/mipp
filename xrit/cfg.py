#
#
#
import os
import re
from ConfigParser import ConfigParser

__all__ = ['read_config',
           'SatConfigReaderError']

class SatConfigReaderError(Exception):
    pass

def read_config(satname, instrument=''):
    return _ConfigReader(satname, instrument)

class _ConfigReader(object):

    def __init__(self, satname, instrument=''):
        try:
            home = os.environ['PPP_CONFIG_DIR']
        except KeyError:
            raise SatConfigReaderError("PPP_CONFIG_DIR environment variable is not set")

        self.config_file = home + '/' + satname + '.cfg'
        if not os.path.isfile(self.config_file):
            raise SatConfigReaderError("Unknown satellite: '%s' (no such file: '%s')"%(satname, self.config_file))
        self._config = ConfigParser()
        self._config.read(self.config_file)
        
        instruments = self.get('satellite')['instruments']
        if not instrument:
            if len(instruments) == 1:
                instrument = instruments[0]
            else:
                raise SatConfigReaderError("Please specify instrument")
        else:
            if instrument not in instruments: 
                raise SatConfigReaderError("Unknown instrument: '%s'"%instrument)
        self.instrument = instrument
        
        self._channels = self._channels2dict(instrument)

    def __call__(self, section):
        return self.get(section)

    def get(self, section):
        options = {}
        if section != 'satellite' and not section.startswith(self.instrument):
            section = self.instrument + '-' + section
        for k, v in self._config.items(section, raw=True):
            options[k] = _eval(v)
        return options

    def get_channels(self):
        return self._channels

    def get_channel(self, channel):
        try:
            return self._channels[channel]
        except KeyError:
            raise SatConfigReaderError("Unknown channel: '%s'"%channel)

    def get_channel_names(self):
        return sorted(self._channels.keys())

    def _channels2dict(self, instrument):
        rec = re.compile('^%s-\d+$'%instrument)
        channels = {}
        for sec in self._config.sections():
            if rec.findall(sec):
                c = _Channel(self._config.items(sec, raw=True))
                channels[c.name] = c
        return channels
    
class _Channel:
    def __init__(self, kv):
        for k, v in kv:
            setattr(self, k, _eval(v))
    def __str__(self):
        keys = sorted(self.__dict__.keys())
        s = ''
        for k in keys:
            if k[0] == '_':
                continue
            v = getattr(self, k)
            if k == 'resolution':
                v = "%.2f"%v
            elif k == 'frequency':
                v = "(%.2f, %.2f, %.2f)"%v
            s += k + ' = ' + str(v) + ', '
        return s[:-2]    

def _eval(v):
    try:
        return eval(v)
    except:
        return str(v)

if __name__ == '__main__':
    import sys
    cfg = read_config(sys.argv[1], 'mviri')
    print cfg('satellite')
    print cfg('level1')
    cs = cfg.get_channels()
    for k in sorted(cs.keys()):
        print cs[k]
