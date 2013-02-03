#from .audioCodec import * #TODO: finish this module
from .cpuCodec import *
from .ramCodec import *
from .swapCodec import *
from .systemCodec import *

__all__ = ['CpuCodec','RamCodec','SwapCodec', 'SystemCodec']

try:
    import yaml
except ImportError:
    ImportError('Python 3 yaml library required.')

class CpuCodec(CpuCodec):
    pass

class RamCodec(RamCodec):
    pass

class SwapCodec(SwapCodec):
    pass

class SystemCodec(SystemCodec):
    pass