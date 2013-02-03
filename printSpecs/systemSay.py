#!/usr/bin/python3

# utility program to test Spectacles

try:
    import yaml
except ImportError:
    ImportError('Python 3 yaml library required.')

from Spex import SystemCodec

class SystemSay(object):

    def __init__(self):
        self = self
        self.specsCodec = SystemCodec()
        self.specsEncode = self.specsCodec.encode()
    #end

    # private
    def __print_dict(self, dict, level):
        keys = list(dict.keys())
        keys.sort()
        line = ''

        for key in keys:
            if level == 'full':
                line = line + str(key) + ': ' + str(dict[key]) + 'MHz '
            if level == 'simple':
                line = str(dict[key])

        return line.strip()
    #end

    # public
    def say(self, printLevel):

#        if len(printLevel) > 1:
#            self.printLevel = printLevel[1]
#        else:
#            self.printLevel = printLevel

#        sys = SystemCodec()
#        sysEncode = sys.encode()
        
        # convert yaml object to dictionary
        systemYaml  = yaml.load(self.specsEncode)
        systemInfo  = systemYaml['system']
        cpuInfo     = systemInfo['processor']
        cpuBrand    = cpuInfo['brand']
        socketCount = cpuInfo['socket']['count']['alpha']
        coreCount   = cpuInfo['cores']['count']['alpha']
        HT          = ('-HT' if cpuInfo['hyperthread'] else '')
        MCP         = ('-MCP' if (cpuInfo['cores']['count']['numeric'] > 1) else '')
        SMP         = ('-SMP' if (cpuInfo['socket']['count']['numeric'] > 1) else '')
        UP          = ('-UP' if ((cpuInfo['socket']['count']['numeric'] == 1) and \
                        (cpuInfo['cores']['count']['numeric'] == 1)) else '')
        procInfo    = " (" + HT + MCP + SMP + UP + "-) "

        memInfo     = systemInfo['memory']
        memTotal    = memInfo['total']
        memFree     = memInfo['free']
        memBuffer   = memInfo['buffer']
        memCache    = memInfo['cache']
        memUsed     = memInfo['used']
        memUnused   = memInfo['unused']

#        swapInfo    = systemInfo['swap']
#        swapTotal   = swapInfo['total']
#        swapFree    = swapInfo['free']
#        swapUsed    = swapInfo['used']

        processorFull = "CPU:       Processor:      [ " + \
            socketCount + "-Socket " + \
            coreCount + "-Core " + \
            cpuBrand + \
            procInfo + "]"
        cacheFull     = "           Cache:          "   + '[ ' + self.__print_dict(cpuInfo['cache'], 'full') + ' ]'
        flagsFull     = "           Flags:          "   + '[ ' + cpuInfo['flags'] + ' ]'
        clocksFull    = "           Core Speeds:    "   + '[ ' + self.__print_dict(cpuInfo['cores']['frequency']['core'], 'full') + ' ]'
        minMaxFreq    = "           Min/Max Speeds: [ " + str(cpuInfo['cores']['frequency']['min']) + 'MHz' + \
            " : " + str(cpuInfo['cores']['frequency']['max']) + 'MHz' + " ]"

        memoryFull    = "RAM:       Memory:         [ " + \
            "Total: " + memTotal + "MB" + \
            " | Free: " + memFree + "MB" + \
            " | Used: " + memUsed + "MB" + \
            " | Buffer: " + memBuffer + "MB" + \
            " | Cache: " + memCache + "MB" + \
            " | Unused: " + memUnused + "MB" + " ]"

#        swapFull      = "SWAP:      Swap:           [ " + \
#            "Total: " + swapTotal + "MB" + \
#            " | Free: " + swapFree + "MB" + \
#            " | Used: " + swapUsed + "MB" + " ]"

        if printLevel == '-F':
            print(processorFull)
            print(cacheFull)
            print(flagsFull)
            print(clocksFull)
            print(minMaxFreq)
            print(memoryFull)
#            print(swapFull)
        elif printLevel == '-Y':
            self.yamlSay()
        else:
            print("CPU:[ " + socketCount + "-Socket " + \
                coreCount + "-Core " + \
                cpuBrand + \
                procInfo + \
                clocksFull)
    #end

    # public
    def yamlSay(self):
        print(self.specsEncode)
    #end

#end class
