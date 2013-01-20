#! /usr/bin/python3

import yaml
from Specs.cpu import Cpu

class CpuCodec(object):
    """ Encodes specs output to yaml object.
        or
        Decodes yaml objects to python dictionaries"""

    def __init__(self):
        self = self
        cpu = Cpu()
        self.brand              = cpu.brand()
        self.model              = cpu.model()
        self.bits               = cpu.bits()
        self.isHt               = cpu.isHT()
        self.isUP               = cpu.isUP()
        self.isSMP              = cpu.isSMP()
        self.isMCP              = cpu.isMCP()
        self.cacheDict          = cpu.cache()
        self.flags              = cpu.flags()

        self.socketCount        = cpu.socket.count.num()
        self.socketAlphaCount   = cpu.socket.count.alpha()

        self.realCoreCount      = cpu.core.count.num.real()
        self.rawCoreCount       = cpu.core.count.num.raw()
        self.coreAlphaCount     = cpu.core.count.alpha()

        self.coreFrequencyList  = cpu.core.frequency.list()
        self.minFrequency       = cpu.core.frequency.min()
        self.maxfrequency       = cpu.core.frequency.max()
    #end

#        isHT    # if core siblings group repeats
#        isUP    # if socket = 1 and core = 1
#        isSMP   # if socket > 1
#        isMCP   # if core > 1

    def encode(self):
        """ Creates a yaml object of the system processor."""
        
        cpuInfo     = {}
        cores       = {}
        coreCount   = {}
        coreSpeeds  = {}
        socket      = {}
        socketCount = {}

        cpuInfo['brand']        = self.brand
        cpuInfo['model']        = self.model
        cpuInfo['bits']         = self.bits
        cpuInfo['socket']       = socket
        cpuInfo['hyperthread']  = True if self.isHt else False
        cpuInfo['cores']        = cores
        cpuInfo['cache']        = self.cacheDict
        cpuInfo['flags']        = self.flags

        socket['count']         = socketCount
        
        socketCount['numeric']  = self.socketCount
        socketCount['alpha']    = self.socketAlphaCount

        cores['count']          = coreCount
        cores['frequency']      = coreSpeeds

        coreCount['numeric']    = self.realCoreCount
        coreCount['alpha']      = self.coreAlphaCount

        coreSpeeds['core']      = self.coreFrequencyList
        coreSpeeds['min']       = self.minFrequency
        coreSpeeds['max']       = self.maxfrequency

        return yaml.dump(cpuInfo, default_flow_style=False)
    #end

    def decode(self):
        pass
    #end
#end
