#!/usr/bin/python

#
#  Copyright (C) 2011 W. Scott Rogers
#
#  This program is free software.
#  You can redistribute it and/or modify it under the terms of the
#  GNU General Public License as published by the Free Software Foundation;
#  either version 2 of the License.
#  Please read the COPYING file.

try:
    import yaml
except ImportError:
    ImportError('Python 3 yaml library required.')

from Spex import Cpu, CpuCodec

class CpuSayPy2:

    def __init__(self):
        self = self
    #end

    @staticmethod
    def __printDict(dict, level):
        keys = list(dict.keys())
        keys.sort()
        line = ''

        for key in keys:
            if level == 'full':
                line = line + "[ " + str(key) + ": " + str(dict[key]) + " ] "
            if level == 'simple':
                line = str(dict[key])

        return line.strip()
    #end

    @staticmethod
    def get_print_data(level):
        cpu_data_dict = {}

        isHT    = Cpu.isHyperThreaded()
        isUP    = Cpu.isUniprocessor()
        isSMP   = Cpu.isSymetricalMultiProcessor()
        isMCP   = Cpu.isMultiCoreProcessor()

        cpu_data_dict['cpuHtState']      = '-HT' if isHT else ''
        cpu_data_dict['cpuMcpState']     = '-MCP' if isMCP else ''
        cpu_data_dict['cpuSmpState']     = '-SMP' if isSMP else ''
        cpu_data_dict['cpuUniProcessor'] = '-UP' if isUP else ''

        cpu_data_dict['socketCount']     = str(Cpu.getSocketAlphaCount())
        cpu_data_dict['coreCount']       = str(Cpu.getCoreAlphaCount())
        cpu_data_dict['cpuBrand']        = str(Cpu.getBrand())
        cpu_data_dict['cache']           = str(CpuSayPy2.__printDict(Cpu.getRawCache(), level))
        cpu_data_dict['frequencies']     = str(CpuSayPy2.__printDict(Cpu.getCoreFreq(), level))
        cpu_data_dict['flags']           = str(Cpu.getFlags())
        cpu_data_dict['cpuMaxFreq']      = str(Cpu.getMaxFrequency())
        cpu_data_dict['cpuMinFreq']      = str(Cpu.getMinFrequency())

        return cpu_data_dict
    #end

    @staticmethod
    def fullSay():
        cpuDataList = CpuSayPy2.get_print_data('full')
        processorFull = "CPU:       Processor:      [ " + cpuDataList['socketCount'] + \
                        "-Socket " + cpuDataList['coreCount'] + "-Core " + \
                        cpuDataList['cpuBrand'] + " (" + cpuDataList['cpuHtState'] + \
                        cpuDataList['cpuMcpState'] + cpuDataList['cpuSmpState'] + \
                        cpuDataList['cpuUniProcessor'] + "-) ]"
        cacheFull     = "           Cache:          "   + cpuDataList['cache']
        flagsFull     = "           Flags:          "   + cpuDataList['flags']
        clocksFull    = "           Core Speeds:    "   + cpuDataList['frequencies']
        minMaxFreq    = "           Min/Max Speeds: [ " + cpuDataList['cpuMinFreq'] + " : " + cpuDataList['cpuMaxFreq'] + " ]"

        print(processorFull)
        print(cacheFull)
        print(flagsFull)
        print(clocksFull)
        print(minMaxFreq)
    #end

    @staticmethod
    def simpleSay():
        cpuDataList = CpuSayPy2.get_print_data('simple')
        print("CPU:[ " + cpuDataList['socketCount'] + "-Socket " + cpuDataList['coreCount'] + \
                "-Core " + cpuDataList['cpuBrand'] + " (" + cpuDataList['cpuHtState'] + \
                        cpuDataList['cpuMcpState'] + cpuDataList['cpuSmpState'] + \
                        cpuDataList['cpuUniProcessor'] + "-) " + cpuDataList['frequencies'] + "MHz ]")
    #end

    @staticmethod
    def yamlSay():

        codec = CpuCodec()

        system = {}
        system['system'] = yaml.load(codec.encode())
        systemYaml  = yaml.dump(system)

        print(systemYaml)
    #end
#end class
