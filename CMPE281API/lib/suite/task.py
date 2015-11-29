#!/usr/bin/python

from static import ag

scoreMap = {
   "groups":[
        {
            "type": "phone",
            "weight" : 5, 
            "message" : "bla",
            "permissions":[]
         },
        {
            "type" : "phone",
            "weight" : 10,
            "message" : "can make phone call or SMS",
	    "permissions":[
                "CALL_PHONE", "CALL_PRIVILEGED", "SEND_SMS"
            ]
        },
        {
            "type": "media",
            "weight" : 5,
            "message" : "can capture audio video",
            "permissions":["CAPTURE_AUDIO_OUTPUT", "CAPTURE_SECURE_VIDEO_OUTPUT", "CAPTURE_VIDEO_OUTPUT"]
         },
        {
            "type": "config",
            "weight" : 15,
            "message" : "can change configuration",
            "permissions":["CLEAR_APP_CACHE", "DUMP", "MODIFY_PHONE_STATE", "MODIFY_AUDIO_SETTINGS", "MOUNT_UNMOUNT_FILESYSTEMS", "CHANGE_CONFIGURATION", "CHANGE_NETWORK_STATE", "CHANGE_WIFI_MULTICAST_STATE", "CHANGE_WIFI_STATE"]
         },
        {
            "type": "risky",
            "weight" : 10,
            "message" : "has risky permissions",
            "permissions":["GET_ACCOUNTS", "GET_PACKAGE_SIZE", "GLOBAL_SEARCH", "INSTALL_PACKAGES", "KILL_BACKGROUND_PROCESSES", "REBOOT"]
         },
        {
            "type": "network",
            "weight" : 2,
            "message" : "has network access",
            "permissions":["INTERNET", "ACCESS_NETWORK_STATE", "ACCESS_WIFI_STATE"]
         },
        {
            "type": "userdata",
            "weight" : 10,
            "message" : "can access user data",
            "permissions":["READ_CALENDAR", "READ_CALL_LOG", "READ_CONTACTS", "READ_EXTERNAL_STORAGE", "READ_SMS", "READ_VOICEMAIL", "WRITE_CALENDAR", "WRITE_CALL_LOG", "WRITE_CONTACTS", "WRITE_VOICEMAIL", "ADD_VOICEMAIL"]
         },
    ]
}
permission_weights = {'android.permission.WRITE_EXTERNAL_STORAGE': 0.01,
                      'android.permission.INTERNET': 0.00, 
                      'android.permission.ACCESS_NETWORK_STATE': 0.00, 
                      'android.permission.KILL_BACKGROUND_PROCESSES': 0.85, 
                      'android.permission.WRITE_SETTINGS': 0.50, 
                      'android.permission.READ_LOGS': 0.30, 
                      'android.permission.RECEIVE_BOOT_COMPLETED': 0.05, 
                      'android.permission.READ_PHONE_STATE': 0.05, 
                      'android.permission.CALL_PHONE': 0.03, 
                      'android.permission.READ_CONTACTS': 0.05, 
                      'android.permission.WRITE_CONTACTS': 0.09, 
                      'android.permission.READ_SMS': 0.03, 
                      'android.permission.WRITE_SMS': 0.03, 
                      'android.permission.RECEIVE_SMS': 0.03, 
                      'android.permission.RECEIVE_MMS': 0.03, 
                      'android.permission.SEND_SMS': 0.03, 
                      'android.permission.GET_PACKAGE_SIZE': 0.00, 
                      'android.permission.PROCESS_OUTGOING_CALLS': 0.55, 
                      'com.android.browser.permission.READ_HISTORY_BOOKMARKS': 0.69, 
                      'android.permission.MODIFY_PHONE_STATE': 0.90, 
                      'android.permission.GET_TASKS': 0.05, 
                      'android.permission.READ_CALL_LOG': 0.30, 
                      'android.permission.WRITE_CALL_LOG': 0.30, 
                      'android.permission.GET_ACCOUNTS': 0.10, 
                      'android.permission.MANAGE_ACCOUNTS': 0.50, 
                      'com.android.vending.BILLING': 0.01, 
                      'android.permission.USE_CREDENTIALS': 0.10, 
                      'android.permission.CHANGE_WIFI_STATE': 0.07, 
                      'android.permission.BATTERY_STATS': 0.00, 
                      'android.permission.ACCESS_WIFI_STATE': 0.00, 
                      'android.permission.VIBRATE': 0.00, 
                      'android.permission.PACKAGE_USAGE_STATS': 0.00, 
                      'android.permission.ACCESS_SUPERUSER': 0.99, 
                      'android.permission.WAKE_LOCK': 0.10, 
                      'android.permission.ACCESS_FINE_LOCATION': 0.05, 
                      'com.google.android.gms.permission.ACTIVITY_RECOGNITION': 0.32
                    }
class Task(object):

    def __init__(self, apk_path):
        self.apk_path = apk_path
    
    def calculate_perm_weight(self, permissions):
        calculated_score = 100
        for perm in permissions:
            if perm in permission_weights.keys():
 	        calculated_score *= (1 - permission_weights[perm])
        calculated_score = 1 if calculated_score < 1 else calculated_score
	return round(calculated_score)

    def computeScore(self, permissions):
        global scoreMap
        result = {}
        result["score"] = len(permissions)
        result["details"] = ""
        types = {}

        for permission in permissions:
            key = permission.split(".")[-1]
            for group in scoreMap["groups"]:
                if key in group["permissions"]:
                    result["score"] += group["weight"]
                    if not group["type"] in types:
                        result["details"] += group["message"] + ", "
                        types[group["type"]] = 1;

        if len(result["details"]) > 0:
            result["details"] = "This app " + result["details"].strip(', ') + ". Total permissions:" + str(len(permissions))

        if result["score"] > 100:
            result["score"] = 100

        return result
                    
        

    def analyze(self, test_type):
	test_type = test_type.lower()
	test = None
        if test_type == "static":
	    test = ag.StaticAnalysis()
        elif test_type == "dynamic":
            raise NotImplementedError("Not ready yet")
        else:
            raise Exception("no such test type: {0}".format(test_type))
        test.load_apk(self.apk_path)
        permissions = test.analyze_permissions()
        return self.computeScore(permissions)

if __name__ == "__main__":
    t = Task("apks/com.twitter.android/app.apk");
    print t.analyze("static")

