#!/usr/bin/python3

try:
    import yaml
except ImportError:
    ImportError('Python 3 yaml library required.')

import re
import sys

class BaseRay(object):
    """
    Base utility to import yaml config files
    """

    def __init__(self):
        self = self
    #end

    # public
    def set_file(self, file):
        """
        Set the configuration file.
        """
        self.specFile = '{0}/{1}'.format(sys.path[0], file)
    #end

    # public
    def get_file(self):
        """
        Return the set configuration file.
        """
        return self.specFile
    #end

    def load(self):
        """
        Load the spec file
        """
        self.specConf = yaml.load(open(self.specFile, 'r'))
    #end

    # public
    def set_type(self, type):
        """
        Sets the specification type.
        """
        self.specType = type
    #end

    # public
    def get_type(self):
        pass
    #end

    # public
    def file_proc_info(self):
        """
        Public: returns the kernel's cpu info file
        """
        return self.get_file_contents(self.specConf['info'])
    #end

    # public
    def get_file_contents(self, file):
        """ Returns the contents of system files"""
        with open(file, "r") as someFile:
            return someFile.readlines()
    #end

    # public
    def clean_list(self, item):
        for banItem in self.specConf['banList']:
            item = re.sub(banItem, '', item)
        return self.sanitize_list(item)
    #end

    # public
    def sanitize_list(self, item):
        item = re.sub(',', " ", item)
        item = re.sub('^ +| +$', "", item)
        item = re.sub(' [ \t]+', " ", item)

        return self.remove_extra_whitespace(item)
    #end

    # public
    def remove_extra_whitespace(self, item):
        while '  ' in item:
            item = item.replace('  ', ' ')
        return item.rstrip()
    #end

    # public
    def get_info_dict(self):
        """ A private method to read in the info file and return a dictionary."""
        infoDict = {}

        for item in self.file_proc_info():
            if len(item) > 1:
                key, value = item.split(':')
                infoDict[key.strip('\r\t')] = value.strip('\r\n').strip()
        return infoDict
    #end
#end
