#!/usr/bin/python

from androguard.core.bytecodes.apk import APK

import os


class StaticAnalysis:

    def __init__(self):
        print "Static Analysis"
        self.apk = None     
   
    def load_apk(self, apk):
        if apk is not None and os.path.isfile(apk):
	    self.apk = APK(apk)
        else:
	    raise IOError("{0} could not be loaded".format(apk))

    def get_apk_package(self):
        try:
	    return self.apk.get_package()
	except Exception, e:
	    raise e

    def analyze_permissions(self):
        try: 
	    return self.apk.get_permissions()
	except Exception, e:
	    raise e


