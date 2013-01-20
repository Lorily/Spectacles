#!/usr/bin/python3

import yaml
from Specs.abstract.linux.baseAbs import BaseAbs

class RamAbs(BaseAbs):

    def __init__(self, specFile = 'Specs/abstract/linux/configuration/ram.configuration.yml'):
        self = self
        self.set_file(specFile)
    #end

    def read(self):
        """
        Read the ram. Meminfo is already in a dictionary like state. Yaml helps
        translate quicker.
        """
        self.meminfo = yaml.load(open(self.specConf['info'], 'r'))
#end class
