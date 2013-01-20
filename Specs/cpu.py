#!/usr/bin/python3
# Interface/API

from Specs.liaison.cpuLia import CpuLia

class Cpu(object):
    """ Class performs actions to create dictionaries"""

    ## The order is important
    def __init__(self):
        self            = self
        self.liaison    = CpuLia()
        self.socket     = Socket(self.liaison)
        self.core       = Core(self.liaison)

    def brand(self):
        """
        The cpu brand.
        """
        return self.liaison.get_brand()
    #end

    def isHT(self):
        """
        Boolean: true for hyperthreading, false otherwise.
        """
        return self.liaison.is_hyperthreaded()
    #end

    def isUP(self):
        """
        Boolean: true for single core single socket cpu systems.
        """
        return self.liaison.is_uniprocessor()
    #end

    def isMCP(self):
        """
        Boolean: true for multicore processors.
        """
        return self.liaison.is_multi_core_processor()
    #end

    def isSMP(self):
        """
        Boolean: for symetrical multiprocessors.
        """
        return self.liaison.is_symetrical_multi_processor()
    #end

    def model(self):
        """
        The cpu model.
        """
        return self.liaison.get_model()
    #end

    def bits(self):
        """
        The cpu bits: 32/64.
        """
        return self.liaison.get_bits()
    #end

    def cache(self):
        """
        The cpu cache by level.
        """
        return self.liaison.get_raw_cache_dict()
    #TODO: return unified cache?

    def flags(self):
        """
        The cpu flags.
        """
        return self.liaison.get_flags()


class Core(object):
    """
    Cpu cores.
    """

    def __init__(self, liaison):
        self            = self
        self.liaison    = liaison
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
            return self.core.liaison.get_core_freq_list()
        #end

        def min(self):
            """
            Minimum cpu core frequency.
            """
            return self.core.liaison.get_min_frequency()
        #end

        def max(self):
            """
            Maximum cpu core frequency.
            """
            return self.core.liaison.get_max_frequency()
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
            return self.core.liaison.get_core_alpha_count()
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
                return self.count.core.liaison.get_real_core_count()
            #end

            def raw(self):
                """
                All cores. Includes HT cores.
                """
                return self.count.core.liaison.get_raw_core_count()
            #end
        #end
    #end
#end

class Socket(object):
    """
    Cpu socket class.
    """
    def __init__(self, liaison):
        self = self
        self.liaison = liaison
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
            return self.socket.liaison.get_socket_alpha_count()

        def num(self):
            """
            Numeric number of sockets.
            """
            return self.socket.liaison.get_socket_count()
    #end
#end