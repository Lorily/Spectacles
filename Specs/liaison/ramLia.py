#! /usr/bin/python3
# Liaison

from Specs.abstract.linux.ramAbs import RamAbs

class RamLia(object):
    """ Class performs actions to create dictionaries"""

    def __init__(self):
        self = self
        self.abstract = RamAbs()
        self.abstract.load()
        self.abstract.read()
    #end

################################################################################
##
##  Public methods for API use.
##
################################################################################

    def get_total_ram(self):
        """
        Total ram reported by system
        """
        return int(self.__clean(self.abstract.meminfo['MemTotal']))/1024
    #end

    def get_unused_ram(self):
        """
        Free ram reported by system
        """
        return int(self.__clean(self.abstract.meminfo['MemFree']))/1024
    #end

    def get_buffered_ram(self):
        """
        Buffered ram.  Easily freed by kernel for application use when needed.
        """
        return int(self.__clean(self.abstract.meminfo['Buffers']))/1024
    #end

    def get_cached_ram(self):
        """
        Cached ram.  Application and kernel cache.  Easily freed by kernel for
        application use when needed.
        """
        return int(self.__clean(self.abstract.meminfo['Cached']))/1024
    #end

    def get_free_ram(self):
        """
        Free + buffered + cached.   Easily freed by kernel for application use
        when needed.
        """
        return  (int(self.get_unused_ram()) + \
                int(self.get_buffered_ram()) + \
                int(self.get_cached_ram()))
    #end

    def get_used_ram(self):
        """
        Total - (Free + buffered + cached).   Easily freed by kernel for
        application use when needed.
        """
        return  (int(self.get_total_ram()) - \
                int(self.get_free_ram()))

    def get_swap_total(self):
        """
        The total available swap size available to the kernel.
        """
        return int(self.__clean(self.abstract.meminfo['SwapTotal']))/1024
    #end

    def get_swap_free(self):
        """
        Amount of swap space free for use by the kernel.
        """
        return int(self.__clean(self.abstract.meminfo['SwapFree']))/1024
    #end

    def get_swap_used(self):
        """
        Amount of swap space used by the kernel.
        """
        return int(int(self.get_swap_total()) -\
                int(self.get_swap_free()))
        #end

    def __clean(self, value):
        """
        Utility to get only numbers.
        """
        return int(str(value).split(' ')[0])
    #end
