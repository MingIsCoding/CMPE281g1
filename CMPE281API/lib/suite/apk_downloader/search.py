#!/usr/bin/python

# Do not remove
GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

import sys
from pprint import pprint

from config import *
from googleplay import GooglePlayAPI
from helpers import sizeof_fmt, print_header_line, print_result_line

def findAppInfo(packageName):
    request = packageName
    nb_res = None
    offset = None

    api = GooglePlayAPI(ANDROID_ID)
    api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)

    try:
        message = api.search(request, nb_res, offset)
        doc = message.doc[0]
        for c in doc.child:
            if c.docid.startswith(packageName):
                result = {}
                result["creator"] = c.creator
                result["price"] = c.offer[0].formattedAmount
                return result
    except Exception, e:
        print str(e)

    return None

if __name__ == "__main__":
    print (str(findAppInfo("com.twitter.android")))
