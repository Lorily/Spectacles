#!/usr/bin/python3
# Abstract

import os
from .baseRay import BaseRay

class CpuRay(BaseRay):
    """
    Cpu util to parse system according to settings in configuration file.
    """

    def __init__(self, specFile = 'Spex/xRay/linux/configuration/cpu.configuration.yml'):
        BaseRay.__init__(self)
        self = self
        self.set_file(specFile)
    #end

    def clean_cpu_list(self, item):
        """
        List of lists used to clean passed object. Removes items from ban lists.
        """
        return self.clean_list(item)
    #end

    # public
    def file_siblings(self):
        """
        Public: returns core siblings. Important for detecting hyperthreading.
        """
        return self.get_file_contents('{0}/cpu0{1}'.format(
            self.specConf['system'],
            self.specConf['threadSiblingsList']
        ))
    #end

    # public
    def file_sys_cpu(self):
        """
        Public: returns the number of cores present. Includes virtual cores.
        """
        return self.get_file_contents(self.specConf['present'])
    #end

    # public
    def file_cpu_max_freq(self):
        """
        Public: returns the maximum cpu speed file.
        """
        return self.get_file_contents(self.specConf['maxFreq'])
    #end

    # public
    def file_cpu_min_freq(self):
        """
        Public: returns the minimum cpu speed file.
        """
        return self.get_file_contents(self.specConf['minFreq'])
    #end

    # public
    def max_cache_level(self):
        """
        Public: returns the number of cache levels.
        """
        return len(os.listdir('{0}/{1}'.format(
            self.specConf['system'],
            self.specConf['cache']
        )))
    #end

    # public
    def sys_cpu_socket_id(self, count):
        """
        Public: returns the returns the id of the specified core's socket.
        """
        return self.get_file_contents('{0}/cpu{1}{2}'.format(
            self.specConf['system'],
            str(count),
            self.specConf['pysicalId']
        ))
    #end

    # public
    def sys_cpu_core_freq(self, count):
        """
        Public: returns the specified core's frequency.
        """
        return self.get_file_contents('{0}/cpu{1}{2}'.format(
            self.specConf['system'],
            str(count),
            self.specConf['currentFreq']
        ))
    #end

    # public
    def sys_cpu_cache_level(self, index):
        """
        Public: returns the cache at the specfied level.
        """
        return self.get_file_contents('{0}/{1}/index{2}{3}'.format(
            self.specConf['system'],
            self.specConf['cache'],
            str(index),
            self.specConf['cacheSize']
        ))
    #end
#end
