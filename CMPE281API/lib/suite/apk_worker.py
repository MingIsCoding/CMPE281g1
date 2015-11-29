import psycopg2
import os
import time
import task
import sys
import traceback

sys.path.append('../')

from database.psql import DatabaseDriver
from apk_downloader import download, search


def logit(message):
    print("APKWorker:" + message)

def getAppInfo(packageName):
    result = {}
    result["offmkt"] = True
    result["price"] = -1;

    for i in range(1, 5):
        appInfo = None
        try:
            appInfo = search.findAppInfo(packageName)
            break
        except:
            print "getAppInfo: Sleeping to make Google Happy"
            time.sleep(60)
            continue
    if appInfo:
        result["offmkt"] = False
        if appInfo["price"] == "Free":
           result["price"] = 0;
        else:
           result["price"] = appInfo["price"]

    return result

def downloadApk(package, targetFolder):
    if not os.path.isdir(targetFolder):
        os.makedirs(targetFolder)
    if os.path.isdir(targetFolder):
        targetFile = targetFolder + "/app.apk"
        logit("downloadApk: package:" + package + " targetFile:" + targetFile)
        if not os.path.isfile(targetFile):
            for i in range(1, 5):
                try:
                    download.download_apk(package, targetFile)
                    break
                except:
                    print "downloadApk: Sleeping to make Google Happy"
                    time.sleep(60)
                    continue
                
        else:
            logit("downloadApk: file already exists:")
        return targetFile
    else:
        logit("downloadApk: ERR: unable to create the download folder")

def analyzeApk(apkPath):
    try:
        logit("analyzeApk: apkPath:" + apkPath)
        analyzer = task.Task(apkPath)
        return analyzer.analyze("static")
    except:
        return {"score": 0, "details": "Could not analyze"}

def updateAppEntry(db, id, score, message):
    logit('updateAppEntry: updating record:' + str(id))
    sql = "UPDATE Apps SET Score='%d', Message='%s' WHERE id='%d'" % (score, message, id);
    db.execute(sql)


def sweep(dbIn):

    db = dbIn.cursor()

    sql = "SELECT * FROM Apps WHERE Score = 999"
    logit("sweep: sql:" + sql)

    db.execute(sql)
    rows = db.fetchall()
    if not rows:
        logit("sweep: Im bored");
        return
    logit("sweep: DB returned " + str(len(rows)) + " rows")
    for row in rows:
        id = row[0]
        pkgName = row[1]
        
        dbIn.commit() 
        time.sleep(2);
       
        appInfo = getAppInfo(pkgName)
        if appInfo['offmkt']:
            logit("Off Market App - skipping")
            updateAppEntry(db, id, 0, "Off Market App - Score Unknown")
            continue
        if appInfo['price'] != 0:
            logit("Payed App - skipping")
            updateAppEntry(db, id, 0, "Payed App - Cannot analyze");
            continue

        apkFilePath = "./apks/" + pkgName
        logit("sweep: apkFilePath:" + apkFilePath)
        apkFile = downloadApk(pkgName, apkFilePath)
        time.sleep(2);
        if os.path.isfile(apkFile):
            result = analyzeApk(apkFile)
            print result
            updateAppEntry(db, id, result["score"], result["details"]);
        else:
            logit("sweep: ERR: failed to download APK:" + row[1])


def main():
    logit("Opening DB connection")
    with DatabaseDriver() as db:
        while (True):
            try:
                logit("Sweeping..")
                sweep(db)
                db.commit()
            except Exception, e:
                logit("Sweep threw error:" + str(e))
                traceback.print_exc()
            time.sleep(5)


if __name__ == "__main__":
    logit("Starting...")
    main()
    logit("Exiting...")

