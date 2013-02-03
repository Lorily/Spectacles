#! /usr/bin/python3

try:
    import yaml
except ImportError:
    ImportError('Python 3 yaml library required.')

from Spex import Swap

class SwapCodec(object):
    """
    Encodes specs output to yaml object.
    or
    Decodes yaml objects to python dictionaries
    """

    def __init__(self):
        self = self
        swap = Swap()
        self.total  = swap.total()
        self.free   = swap.free()
        self.used   = swap.used()
    #end

    def encode(self):
        """
        Create a yaml object of system swap.
        """
        
        swapInfo = {}

        swapInfo['total']   = str(self.total)
        swapInfo['free']    = str(self.free)
        swapInfo['used']    = str(self.used)

        return yaml.dump(swapInfo, default_flow_style=False)
    #end
#end