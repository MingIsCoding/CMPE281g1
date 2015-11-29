#!/usr/bin/python

from lib.suite import task
from lib.appmagic import AppMagic

my_task = task.Task("sample_apks/slack.apk")
# my_task.analyze("static")
#my_app = AppMagic.get_app_id(package="com.avast.android.mobilesecurity")
#my_task = task.Task("sample_apks/strava.apk".format(my_app['id']))
#print my_app
my_task.analyze("static")
