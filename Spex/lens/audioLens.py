#!/usr/bin/python3

from Spex.xRay import AudioRay

class AudioLens(AudioRay):
    """ Class performs actions to create dictionaries"""

    def __init__(self):
        AudioRay.__init__(self)
        self = self
#        self.util           = AudioUtil()
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
