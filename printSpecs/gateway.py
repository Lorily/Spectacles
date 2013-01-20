#!/usr/bin/python3

# For now, this is a simple file to print out system information
# It is for testing purposes and not meant for production.
# A class method service will be setup to return YAML files

import sys
from printSpecs.systemSay import SystemSay

def main(specArg):
    isPython2 = __pythonVer()

    if isPython2:
        specPy2(specArg)
    else:
        specPy3(specArg)
#end

if __name__ == '__main__':
    main()
#end

def specPy2(specArg):
    """
    Python 2.x support.
    Tested with Python 2.6.5
    """
#    from .printSpecs.cpuSayPy2 import CpuSayPy2
    if len(specArg) > 1:
        if specArg[1] == '-F':
            SystemSay.say('-F')
        if specArg[1] == '-S':
            SystemSay.say('-S')
        if specArg[1] == '-Y':
            SystemSay.yamlSay()
    else:
        SystemSay.say('simple')
#end

def specPy3(specArg):
    """
    Python 3.x support
    """
    systemSay = SystemSay()
    if len(specArg) > 1:
        if specArg[1] == '-F':
            systemSay.say('-F')
        if specArg[1] == '-S':
            systemSay.say('-S')
        if specArg[1] == '-Y':
            systemSay.yamlSay()
    else:
        systemSay.say('simple')
#end

# private
def __pythonVer():
    """Check python version for import
    """
    try:
        if sys.version_info < (3,0):
            return True
        else:
            return False
    except:
        return True
#end
