#!/usr/bin/python3
# Liaison

import re
from Spex.xRay import CpuRay

class CpuLens(CpuRay):
    """ Class reads system cpu/processor information"""

    def __init__(self):
        CpuRay.__init__(self)
        ## The below order is important
        self = self
        self.load()

        self.isHT               = self.is_hyperthreaded()
        self.rawCoreCount       = int(self.get_raw_core_count())
        self.socketCount        = int(self.get_socket_count())
        self.realCoreCount      = int(self.get_real_core_count())
        self.cacheListDict      = self.__get_raw_cache_dict()
        self.unifiedCacheList   = self.__set_unified_cache_level()
        self.brand              = self.get_brand()
    #end

################################################################################
##
##  Public methods for API use.
##
################################################################################

    # public
    def get_core_alpha_count(self):
        """ Returns the alphabetic number of real cores"""
        return self.__get_alpha_count(self.realCoreCount)
    #end

    # public
    def get_socket_alpha_count(self):
        """ Returns the alphabetic number of occupied sockets"""
        return self.__get_alpha_count(self.socketCount)
    #end

    # if ht, then raw_core/2, else raw_core
    # public
    def is_hyperthreaded(self):
        """ Boolean: true if cpu is hyperthreaded"""
        ht = False
        for sibling in self.file_siblings():
            siblings = sibling.split(",")
            if (len(siblings)) > 1 :
                ht = True
        return ht
    #end

    # public
    def get_raw_core_count(self):
        """ Return total core count, including hyperthreaded cores"""
        for line in self.file_sys_cpu():
            core = line.split('-')
            return int(core[len(core) - 1].strip("\r\n")) + 1
    #end

    # public
    def get_real_core_count(self):
        """ Return number of real cores, not hyperthreaded cores"""
        return (self.rawCoreCount/2) if (self.isHT) else (self.rawCoreCount)
    #end

    ## look into removing direct method requests, maybe create a list of socket ID's
    # public
    def get_socket_count(self):
        """ Return total system cpu socket count"""
        oldCpuSocketId = ''
        count = 0
        socketCounter = 0

        while count < self.rawCoreCount:
            sysCpuSocketId = self.sys_cpu_socket_id(count)
            if oldCpuSocketId != sysCpuSocketId:
                oldCpuSocketId = sysCpuSocketId
                socketCounter = socketCounter + 1
            count = count + 1
        return socketCounter
    #end

    # public
    def is_multi_core_processor(self):
        """ Boolean Value. Returns true for multi-core cpus"""
        mcp = False
        if self.realCoreCount > 1:
            if self.socketCount < self.realCoreCount or self.rawCoreCount == self.realCoreCount:
                mcp = True

        return mcp
    #end

    # public
    def is_symetrical_multi_processor(self):
        """ Boolean Value.  Returns true for multi-socket systems"""
        smp = False        
        if self.realCoreCount > 1:
            if self.socketCount == self.realCoreCount:
                smp = True
        return smp
    #end

    # public
    def is_uniprocessor(self):
        """ Boolean value. Returns true for single core, single socket cpus"""
        uniprocessor = False
        if self.realCoreCount == 1:
            uniprocessor = True
        return uniprocessor
    #end

    # public
    def get_core_freq_list(self):
        """ Return a list of core frequencies"""
        sysCpuCoreFreq = {}
        count = 0

        while count < self.realCoreCount:
            eachSysCpuCoreFreq = self.sys_cpu_core_freq(count)
            for freq in eachSysCpuCoreFreq:
                sysCpuCoreFreq[count + 1] = int(freq)//1000
            count = count + 1
        return sysCpuCoreFreq
    #end

    # public
    def get_raw_cache_dict(self):
        """ Return a dictionary of the cache levels"""
        rawCacheDict        = {}
        index = 0
        while index < len(self.cacheListDict):
            if index < 1:
                rawCacheDict['L1'] = str(self.cacheListDict['L' + str(index)]) + " + " + str(self.cacheListDict['L' + str(index)])
    #       Since all x86 cpu's have two L1 caches, we just skip '1'. This will need fixing for non-x86
            if index > 1:
                if self.unifiedCacheList['unifiedL2']:
                    rawCacheDict['L' + str(index)] = str(self.cacheListDict['L' + str(index)])
                elif index == 2:
                    rawCacheDict['L' + str(index)] = str(self.cacheListDict['L' + str(index)] + ' x ' + str(self.realCoreCount))
                elif self.unifiedCacheList['unifiedL3']:
                    rawCacheDict['L' + str(index)] = str(self.cacheListDict['L' + str(index)])
            index = index + 1

        return rawCacheDict
    #end

    # public
    def get_brand(self):
        """ Return the brand of the cpu; ie, AMD, Intel"""
        return self.clean_cpu_list(self.get_info_dict()['model name'])
    #end

    # public
    def get_flags(self):
        """ Return cpu feature flags"""
        flagList    = ""

        for flag in self.get_info_dict()['flags'].split(' '):
            if re.findall('^(lm|nx|pni|svm|vmx|(sss|ss)e+[0-9]?[a-z]?[_]?[0-9]?)', flag):
                flagList = flagList + " " + flag

        return flagList.strip()
    #end

    # public
    def get_max_frequency(self):
        """ Return the cpu's maximum reported frequency"""
        return self.__get_frequency(self.file_cpu_max_freq())
    #end

    # public
    def get_min_frequency(self):
        """ Return the cpu's lowest reported frequency"""
        return self.__get_frequency(self.file_cpu_max_freq())
    #end

    # public
    def get_bits(self):
        """ Return the bit capability of the cpu"""
        pass
    #end

    # public
    def get_model(self):
        """ Return the model of the cpu; ie, T7600"""
        pass
    #end

################################################################################
##
##  Private methods for interanl use.
##
################################################################################


    # private
    def __set_unified_cache_level(self):
        """ Return the unified cache levels. Not per core"""
        maxCacheLevel = self.max_cache_level()
        unifiedL3State  = False
        unifiedL2State  = False

        if maxCacheLevel > 3:
            unifiedL3State = True
        elif maxCacheLevel > 2:
            unifiedL2State = True

        return {'unifiedL2':unifiedL2State, 'unifiedL3':unifiedL3State}
    #end

    # private
    def __get_frequency(self, core):
        """ Return the frequency of core"""
        return int(core[0])/1000
    #end

    # private
    def __get_raw_cache_dict(self):
        """ Return a dictionary of raw caches"""
        maxCacheLevel = self.max_cache_level()
        sysCpuCacheDict = {}

        index = 0
        while index < maxCacheLevel:
            eachSysCpuCacheLevel = self.sys_cpu_cache_level(index)
            for cache in eachSysCpuCacheLevel:
                sysCpuCacheDict['L' + str(index)] = str(cache).strip("\r\n")
            index = index + 1

        return sysCpuCacheDict
    #end

    # public
    def __get_alpha_count(self, count):
        """ Return the alpha word for count"""
        alphaList = ['Single', 'Dual', 'Triple', 'Quad', 'Penta', 'Hexa', 'Hepta', 'Octa', 'Ennea', 'Deca', 'Multi']
        if count > 10:
            count = 11
        return alphaList[count-1]
    #end
#end Class
