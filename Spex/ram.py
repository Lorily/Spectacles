#! /usr/bin/python3
# Interface/API

from .lens import RamLens

class Ram(object):
    """ Class performs actions to create dictionaries"""

    def __init__(self):
        self = self
        self.lens = RamLens()
    #end

    def total(self):
        return format(self.lens.get_total_ram(), '.2f')
    #end

    def buffer(self):
        return format(self.lens.get_buffered_ram(), '.2f')
    #end

    def cache(self):
        return format(self.lens.get_cached_ram(), '.2f')
    #end

    def free(self):
        return format(self.lens.get_free_ram(), '.2f')
    #end

    def unused(self):
        return format(self.lens.get_unused_ram(), '.2f')
    #end

    def used(self):
        return format(self.lens.get_used_ram(), '.2f')
    #end
#end