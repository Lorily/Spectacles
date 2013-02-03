#! /usr/bin/python3

try:
    import yaml
except ImportError:
    ImportError('Python 3 yaml library required.')

from Spex import Ram

class RamCodec(object):
    """
    Encodes specs output to yaml object.
    or
    Decodes yaml objects to python dictionaries
    """

    def __init__(self):
        self = self
        ram = Ram()
        self.total      = ram.total()
        self.free       = ram.free()
        self.buffered   = ram.buffer()
        self.cached     = ram.cache()
        self.used       = ram.used()
        self.unused     = ram.unused()

    #end

    def encode(self):
        """
        Creates a yaml object of system memory.
        """
        
        memInfo = {}

        memInfo['total']    = str(self.total)
        memInfo['free']     = str(self.free)
        memInfo['buffer']   = str(self.buffered)
        memInfo['cache']    = str(self.cached)
        memInfo['used']     = str(self.used)
        memInfo['unused']   = str(self.unused)

        return yaml.dump(memInfo, default_flow_style=False)
    #end
#end
