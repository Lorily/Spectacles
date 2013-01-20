#! /usr/bin/python3

import yaml
from Specs.audio import Audio

class MemCodec(object):
    """ Encodes specs output to yaml object.
        or
        Decodes yaml objects to python dictionaries"""

    def __init__(self):
        self = self
        self.ram = Audio()
    #end

    def encode(self):
        """ Creates a yaml object of audio system."""
        pass
        audioInfo = {}
        return yaml.dump(audioInfo, default_flow_style=False)
    #end

    def decode(self):
        pass
    #end
#end class
