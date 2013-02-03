#!/usr/bin/python3

import yaml
from .baseRay import BaseRay

class RamRay(BaseRay):

    def __init__(self, specFile = 'Spex/xRay/linux/configuration/ram.configuration.yml'):
        BaseRay.__init__(self)
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
