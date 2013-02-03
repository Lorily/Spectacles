#! /usr/bin/python3

from .baseRay import BaseRay

class AudioRay(BaseRay):

    def __init__(self, specFile = 'audio.yml'):
        BaseRay.__init__(self)
        self = self
        self.specFile = specFile
    #end

#end class
