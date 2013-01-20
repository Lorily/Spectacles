#! /usr/bin/python3

from Specs.util.baseUtil import BaseUtil

class MemUtil(BaseUtil):

    def __init__(self, specFile = 'audio.yml'):
        self = self
        self.specFile = specFile
        BaseUtil.__init__(self, specFile)
    #end

#end class
