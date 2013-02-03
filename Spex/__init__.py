from .cpu import *
from .ram import *
from .swap import *
from .codec import *

__all__ = ['Cpu', 'Ram', 'Swap', 'CpuCodec', 'RamCodec', 'SwapCodec', 'SystemCodec']

try:
    import yaml
except ImportError:
    ImportError('Python 3 yaml library required.')

class Cpu(Cpu):
    pass

class Ram(Ram):
    pass

class Swap(Swap):
    pass