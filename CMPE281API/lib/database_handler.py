#!/usr/bin/python

from database.mysqldb import DatabaseDriver

import mysql
import json

class DatabaseHandler(object):

    def __init__(self):
        pass

    @staticmethod
    def createproject(appData):
        parsed_projectData = json.loads(appData)
        projectName = parsed_projectData["projectName"]
        projectStartTime = parsed_projectData["startTime"]
        projectEndTime = parsed_projectData["endTime"]
        projectUserId = parsed_projectData["userId"]
        projectOS = parsed_projectData["projectOS"]
        projectTesterAmount = parsed_projectData["testerAmount"]
        projectAppDownload = parsed_projectData["appDownloadAdd"]
        projectDocDownload = parsed_projectData["docDownloadAdd"]

        with DatabaseDriver() as db:
            cursor = db.cursor()
            try:
                #check if userId exists
                query = "SELECT * FROM Users WHERE userId = (%s)"
                cursor.execute(query, (projectUserId,))
                rows = cursor.fetchall()
                if not rows:
                    return 1000, "userId does not exist.", 0

                #check if projectName exists
                query = "SELECT * FROM Projects WHERE projectName = (%s)"
                cursor.execute(query, (projectName,))
                rows = cursor.fetchall()
                if rows:
                    return 1000, "projectName is already taken.", 0

                #get biggest projectId
                query = "SELECT projectId FROM Projects WHERE projectId = (select MAX(projectId) FROM Projects)"
                print query
                cursor.execute(query)
                last_index = cursor.fetchone()
                print last_index
                if last_index is None:
                    last_index = 0
                else:
                    last_index = last_index[0]
                new_index = int(last_index) + 1

                #insert new project
                data = (new_index, projectName, projectStartTime, projectEndTime, int(projectUserId), projectOS, projectTesterAmount, projectAppDownload, projectDocDownload,)
                query = "INSERT INTO Projects (projectId, projectName, startTime, endTime, userId, projectOS, testerAmount, appDownloadAdd, docDownloadAdd) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)"
                cursor.execute(query, data)
                db.commit()
                return 200, "Project created successfully.", new_index
            except mysql.DatabaseError, e:
                if db:
                    db.rollback()
                return 1000, "Failed to create project.", 0

    @staticmethod
    def createuser(userData):
        parsed_userData = json.loads(userData)
        firstName = parsed_userData["firstName"]
        lastName = parsed_userData["lastName"]
        username = parsed_userData["username"]
        password = parsed_userData["password"]
        roleName = parsed_userData["roleName"]
        email = parsed_userData["email"]
        credit = parsed_userData["credit"]
        money = parsed_userData["money"]
        cardType = parsed_userData["cardType"]
        cardNumber = parsed_userData["cardNumber"]
        csc = parsed_userData["csc"]
        billingAddress = parsed_userData["billingAddress"]
        city = parsed_userData["city"]
        state = parsed_userData["state"]
        zipcode = parsed_userData["zipcode"]
        validDate = parsed_userData["validDate"]
        cardHolder = parsed_userData["cardHolder"]

        with DatabaseDriver() as db:
            cursor = db.cursor()
            try:
                #check if username is unique
                query = "SELECT * FROM Users WHERE username = (%s)"
                cursor.execute(query, (username,))
                rows = cursor.fetchall()
                if rows:
                    return 1000, "Username is already token.", 0

                #check if email is unique
                query = "SELECT * FROM Users WHERE email = (%s)"
                cursor.execute(query, (email,))
                rows = cursor.fetchall()
                if rows:
                    return 1000, "Email is already token.", 0

                query = "SELECT userId FROM Users WHERE userId = (select MAX(userId) FROM Users)"
                cursor.execute(query)
                last_index = cursor.fetchone()
                if last_index is None:
                    last_index = 0
                else:
                    last_index = last_index[0]
                new_index = int(last_index) + 1
                data = (new_index, firstName, lastName, username, password, email, roleName, credit, money, cardType, cardNumber, cardHolder, billingAddress, csc, city, state, zipcode, validDate,)
                query = "INSERT INTO Users (userId, firstName, lastName, username, password, email, roleName, money, credit, cardType, cardNumber, cardHolder, billingAddress, csc, city, state, zipcode, validDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, data)
                db.commit()
                return 200, "User created successfully.", new_index
            except mysql.DatabaseError, e:
                if db:
                    db.rollback()
                return 1000, "Failed to create user.", 0

    @staticmethod
    def loginUser(userData):
        parsed_userData = json.loads(userData)
        username = parsed_userData["username"]
        password = parsed_userData["password"]

        with DatabaseDriver() as db:
            cursor = db.cursor()
            try:
                query = "SELECT * FROM Users WHERE username = (%s) and password = (%s)"
                cursor.execute(query, (username, password,))
                rows = cursor.fetchall()
                if rows:
                    return 200, "Login successfully", 0
                else:
                    return 1000, "Wrong username or password.", 0
            except mysql.DatabaseError, e:
                if db:
                    db.rollback()
                return 1000, "Failed to login user.", 0


    @staticmethod
    def createbug(bugData):
        parsed_bugData = json.loads(bugData)
        bugName = parsed_bugData["bugName"]
        bugLevel = parsed_bugData["bugLevel"]
        causingCondition = parsed_bugData["causingCondition"]
        expectedResult = parsed_bugData["expetedResult"]
        actualResult = parsed_bugData["actualResult"]
        projectId = parsed_bugData["projectId"]
        userId = parsed_bugData["userId"]

        with DatabaseDriver() as db:
            cursor = db.cursor()
            try:
                #check if projectId valid
                query = "SELECT * FROM Projects WHERE projectId = (%s)"
                cursor.execute(query, (projectId,))
                rows = cursor.fetchall()
                if not rows:
                    return 1000, "projectId does not exist.", 0

                #check if userId is valid
                query = "SELECT * FROM Users WHERE userId = (%s)"
                cursor.execute(query, (userId,))
                rows = cursor.fetchall()
                if not rows:
                    return 1000, "userId does not exist.", 0

                query = "SELECT bugId FROM Bugs WHERE bugId = (select MAX(bugId) FROM Bugs)"
                cursor.execute(query)
                last_index = cursor.fetchone()
                if last_index is None:
                    last_index = 0
                else:
                    last_index = last_index[0]
                new_index = int(last_index) + 1
                data = (new_index, bugName, bugLevel, causingCondition, expectedResult, actualResult,(projectId), int(userId),)
                query = "INSERT INTO Bugs (bugId, bugName, bugLevel, causingCondition, expetedResult, actualResult, projectId, userId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, data)
                db.commit()
                return 200, "Bug created successfully.", new_index
            except mysql.DatabaseError, e:
                if db:
                    db.rollback()
                return 1000, "Failed to create bug.", 0

    @staticmethod
    def addUserToProject(inputData):
        parsed_data = json.loads(inputData)
        userId = parsed_data["userId"]
        projectId = parsed_data["projectId"]
        with DatabaseDriver() as db:
            cursor = db.cursor()
            try:
                #check if projectId valid
                query = "SELECT * FROM Projects WHERE projectId = (%s)"
                cursor.execute(query, (projectId,))
                rows = cursor.fetchall()
                if not rows:
                    return 1000, "projectId does not exist.", 0

                #check if userId is valid
                query = "SELECT * FROM Users WHERE userId = (%s)"
                cursor.execute(query, (userId,))
                rows = cursor.fetchall()
                if not rows:
                    return 1000, "userId does not exist.", 0

                #check if entry exist
                query = "SELECT * FROM UserProject WHERE userId = (%s) and projectId = (%s)"
                cursor.execute(query, (userId, projectId,))
                rows = cursor.fetchall()
                if rows:
                    return 1000, "Entry is already exist.", 0

                query = "INSERT INTO UserProject (userId, projectId) VALUES (%s, %s)"
                data = (userId, projectId,)
                cursor.execute(query, data)
                db.commit()
                return 200, "User added to project successfully.", 0
            except mysql.DatabaseError, e:
                if db:
                    db.rollback()
                return 1000, "Failed to create project.", 0

    @staticmethod
    def get_all_projects():
        with DatabaseDriver() as db:
            cursor = db.cursor()
            try:
                query = "SELECT * FROM Projects"
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
            except mysql.DatabaseError, e:
                if db:
                    db.rollback()
                    raise e

    @staticmethod
    def get_all_users():
        with DatabaseDriver() as db:
            cursor = db.cursor()
            try:
                query = "SELECT * FROM Users"
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
            except mysql.DatabaseError, e:
                if db:
                    db.rollback()
                    raise e

    @staticmethod
    def get_users_of_projects(projectData):
        parsed_data = json.loads(projectData)
        projectId = parsed_data["projectId"]
        with DatabaseDriver() as db:
            cursor = db.cursor()
            try:
                query = "SELECT userId FROM UserProject WHERE projectId = (%s)"
                data = (projectId,)
                cursor.execute(query, data)
                rows = cursor.fetchall()
                return rows
            except mysql.DatabaseError, e:
                if db:
                    db.rollback()
                    raise e
    @staticmethod
    def get_project_of_users(userData):
        parsed_data = json.loads(userData)
        projectId = parsed_data["userId"]
        with DatabaseDriver() as db:
            cursor = db.cursor()
            try:
                query = "SELECT projectId FROM UserProject WHERE userId = (%s)"
                data = (projectId,)
                cursor.execute(query, data)
                rows = cursor.fetchall()
                return rows
            except mysql.DatabaseError, e:
                if db:
                    db.rollback()
                    raise e

    @staticmethod
    def get_all_bugs():
        with DatabaseDriver() as db:
            cursor = db.cursor()
            try:
                query = "SELECT * FROM Bugs"
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
            except mysql.DatabaseError, e:
                if db:
                    db.rollback()
                    raise e

    @staticmethod
    def get_bugs(bugData):
        parsed_data = json.loads(bugData)
        projectId = parsed_data["projectId"]
        userId = parsed_data["userId"]
        with DatabaseDriver() as db:
            cursor = db.cursor()
            try:
                if (projectId != "" and userId == ""):
                    query = "SELECT * FROM Bugs WHERE projectId = (%s)"
                    data = (projectId,)
                    cursor.execute(query, data)
                elif (projectId == "" and userId != ""):
                    query = "SELECT * FROM Bugs WHERE userId = (%s)"
                    data = (userId,)
                    cursor.execute(query, data)
                elif (projectId != "" and userId != ""):
                    query = "SELECT * FROM Bugs WHERE (userId, projectId) = (%s, %s)"
                    data = (userId, projectId,)
                    cursor.execute(query, data)
                elif (projectId == "" and userId == ""):
                    query = "SELECT * FROM Bugs"
                    cursor.execute(query)
                else:
                    return None
                rows = cursor.fetchall()
                return rows
            except mysql.DatabaseError, e:
                if db:
                    db.rollback()
                    raise e