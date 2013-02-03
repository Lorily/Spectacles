#!/usr/bin/python3
# API

from .lens import CpuLens

class Cpu(object):
    """ Class performs actions to create dictionaries"""

    ## The order is important
    def __init__(self):
        self            = self
        self.lens    = CpuLens()
        self.socket     = Socket(self.lens)
        self.core       = Core(self.lens)
    #end

    def brand(self):
        """
        The cpu brand.
        """
        return self.lens.get_brand()
    #end

    def isHT(self):
        """
        Boolean: true for hyperthreading, false otherwise.
        """
        return self.lens.is_hyperthreaded()
    #end

    def isUP(self):
        """
        Boolean: true for single core single socket cpu systems.
        """
        return self.lens.is_uniprocessor()
    #end

    def isMCP(self):
        """
        Boolean: true for multicore processors.
        """
        return self.lens.is_multi_core_processor()
    #end

    def isSMP(self):
        """
        Boolean: for symetrical multiprocessors.
        """
        return self.lens.is_symetrical_multi_processor()
    #end

    def model(self):
        """
        The cpu model.
        """
        return self.lens.get_model()
    #end

    def bits(self):
        """
        The cpu bits: 32/64.
        """
        return self.lens.get_bits()
    #end

    def cache(self):
        """
        The cpu cache by level.
        """
        return self.lens.get_raw_cache_dict()
        #TODO: return unified cache?

    def flags(self):
        """
        The cpu flags.
        """
        return self.lens.get_flags()
    #end
#end


class Core(object):
    """
    Cpu cores.
    """

    def __init__(self, lens):
        self            = self
        self.lens    = lens
        self.count      = self.Count(self)
        self.frequency  = self.Frequency(self)
     #end

    class Frequency(object):
        """
        Cpu core frequecy.
        """

        def __init__(self, core):
            self = self
            self.core = core
         #end

        def list(self):
            """
            List of cpu core frequencies.
            """
            return self.core.lens.get_core_freq_list()
        #end

        def min(self):
            """
            Minimum cpu core frequency.
            """
            return self.core.lens.get_min_frequency()
        #end

        def max(self):
            """
            Maximum cpu core frequency.
            """
            return self.core.lens.get_max_frequency()
        #end

    class Count(object):
        """
        Number of cores.
        """

        def __init__(self, core):
            self        = self
            self.core   = core
            self.num    = self.Num(self)
        #end

        def alpha(self):
            """
            Alphabetic number of cores.
            """
            return self.core.lens.get_core_alpha_count()
         #end

        class Num(object):
            """
            Numeric number of cores.
            """

            def __init__(self, count):
                self        = self
                self.count  = count
             #end

            def real(self):
                """
                True cores. Doesn't included HT cores.
                """
                return self.count.core.lens.get_real_core_count()
             #end

            def raw(self):
                """
                All cores. Includes HT cores.
                """
                return self.count.core.lens.get_raw_core_count()
            #end
         #end
    #end
#end

class Socket(object):
    """
    Cpu socket class.
    """
    def __init__(self, lens):
        self = self
        self.lens = lens
        self.count  = self.Count(self)
    #end

    class Count(object):
        """
        Cpu socket counts, either 'alpha' or 'num'.
        """
        def __init__(self, socket):
            self = self
            self.socket = socket
        #end

        def alpha(self):
            """
            Alaphabetic number of sockets.
            """
            return self.socket.lens.get_socket_alpha_count()
        #end

        def num(self):
            """
            Numeric number of sockets.
            """
            return self.socket.lens.get_socket_count()
        #end
    #end
#end