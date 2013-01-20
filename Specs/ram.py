#! /usr/bin/python3
# Interface/API

from Specs.liaison.ramLia import RamLia

class Ram(object):
    """ Class performs actions to create dictionaries"""

    def __init__(self):
        self = self
        self.liaison = RamLia()
    #end

    def total(self):
        return format(self.liaison.get_total_ram(), '.2f')
    #end

    def buffer(self):
        return format(self.liaison.get_buffered_ram(), '.2f')
    #end

    def cache(self):
        return format(self.liaison.get_cached_ram(), '.2f')
    #end

    def free(self):
        return format(self.liaison.get_free_ram(), '.2f')
    #end

    def unused(self):
        return format(self.liaison.get_unused_ram(), '.2f')
    #end

    def used(self):
        return format(self.liaison.get_used_ram(), '.2f')
    #end
#end