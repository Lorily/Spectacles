#!/usr/bin/python3

from Spex import CpuReader

class Cpu(CpuReader):

    def __init__(self):
        self = self
        CpuReader.__init__(self)
    #end

    # public
    def get_brand(self):
        """ Returns the cpu brand, ie Intel, AMD
            TODO: this needs to break out Model to it's own method"""
        return self._get_brand()
    #end

    # public
    def is_hyperthreaded(self):
        """ Boolean, returns true if the cpu is HyperThreaded (virtual cores).
            Usually designates an Intel cpu"""
        return self._is_hyperthreaded()
    #end

    # public
    def isSymetricalMultiProcessor(self):
        """ Boolean, returns true if the system has more than one socket with
            more than one cpu installed."""
        return self.isSymetricalMultiProcessor()
    #end

    # public
    def isMultiCoreProcessor(self):
        """ Boolean, returns true if the processor(s) is(are) multi-core"""
        return self.isMultiCoreProcessor()
    #end

    # public
    def isUniprocessor(self):
        """Boolean, returns true if the system has only one socket and one cpu"""
        return self.isUniprocessor()
    #end

    # public
    def getRawCoreCount(self):
        """ Returns the total number of cores.
            Includes HyperThread cores (vcores)."""
        return self.getRawCoreCount()
    #end

    # public
    def getRealCoreCount(self):
        """ Returns the total number of physical cores.
            Does not include HyperThread cores (vcores)"""
        return reader.getRealCoreCount()
    #end

    # public
    def get_socket_count(self):
        """ Returns the number of occupied sockets on the system.
            SMP would have more than a single socket."""
        return reader._get_socket_count()
    #end

    # public
    def getCoreFreq(self):
        """ Returns a list of the current frequecies of real cores."""
        return reader.getCoreFreq()
    #end

    # public
    def get_raw_cache(self):
        """ Return a list of the all cache per level.
            Returns only up to L3 cache."""
        return reader._get_raw_cache()
    #end

    # public
    def getCoreAlphaCount(self):
        """ Returns the alphabetic number of real cores"""
        return reader.getAlphaCount(self.getRealCoreCount())
    #end

    # public
    def getSocketAlphaCount(self):
        """ Returns the alphabetic number of occupied sockets"""
        return reader.getAlphaCount(self.getSocketCount())
    #end

    # public
    def getModel(self): # not working yet
        """ Returns the cpu Modle, P3, P4, K7, opeteron, etc
            TODO: break model out from brand"""
        pass
    #end

    # public
    def get_flags(self):
        """ Returns a small list of the most common flags."""
        return self._get_flags()
    #end

    # public
    def getMaxFrequency(self):
        """ Returns the cpu's OEM maximum frequency"""
        return self.getMaxFrequency()
    #end

    # public
    def getMinFrequency(self):
        """ Returns the cpu's OEM minimum frequency"""
        return self.getMinFrequency()
    #end

    # public
    def getBits(self):
        """ Returns the processor memory bus width (ie, 32 or 64 bit)"""
        return self.getBits()
    #end

#end Class