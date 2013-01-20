#!/usr/bin/python3

from Specs.util.audioUtil import AudioUtil

class AudioParser(object):
    """ Class performs actions to create dictionaries"""

    def __init__(self):
        self = self
        self.util           = AudioUtil()
        self.audioInfoDict    = self.util.infoDict
    #end

################################################################################
##
##  Public methods for API use.
##
################################################################################



################################################################################
##
##  Private methods for interanl use.
##
################################################################################

#end class
