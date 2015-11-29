from flask import Flask, jsonify, request
from lib.database_handler import DatabaseHandler

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Welcome to Python Flask App!"

@app.route('/createproject', methods=['POST'])
def createproject():
    statusCode, message, projectId = DatabaseHandler.createproject(request.data)
    result = dict()
    result['statusCode'] = statusCode
    result['message'] = message
    if statusCode == 200:
        result['projectId'] = projectId
    return jsonify(result)

@app.route('/createuser', methods=['POST'])
def createuser():
    statusCode, message, userId = DatabaseHandler.createuser(request.data)
    result = dict()
    result['statusCode'] = statusCode
    result['message'] = message
    if statusCode == 200:
        result['userId'] = userId
    return jsonify(result)

@app.route('/createbug', methods=['POST'])
def createbug():
    statusCode, message, bugId = DatabaseHandler.createbug(request.data)
    result = dict()
    result['statusCode'] = statusCode
    result['message'] = message
    if statusCode == 200:
        result['bugId'] = bugId
    return jsonify(result)

@app.route('/addusertoproject', methods=['POST'])
def addUserToProject():
    statusCode, message, userId = DatabaseHandler.addUserToProject(request.data)
    result = dict()
    result['statusCode'] = statusCode
    result['message'] = message
    return jsonify(result)

#get APIs
@app.route('/projects', methods=['GET'])
def get_all_projects():
    raw_projects_data = DatabaseHandler.get_all_projects()
    projects = []
    for projectId, projectName, projectOS, testerAmount, startTime, endTime, userId, appDownloadAdd, docDownloadAdd in raw_projects_data:
        projects.append({"projectId": projectId, "projectName": projectName, "projectOS":projectOS, "testerAmount":testerAmount, "startTime": startTime, "endTime":endTime, "userId":userId, "appDownloadAdd":appDownloadAdd, "docDownloadAdd":docDownloadAdd})
    result = dict()
    result.update({"results":projects})
    return jsonify(result)

@app.route('/userofproject', methods=['POST'])
def get_user_of_project():
    raw_users_data = DatabaseHandler.get_users_of_projects(request.data)
    users = []
    if raw_users_data:
        for userId in raw_users_data:
            users.append({"userId": userId[0]})
    result = dict()
    result.update({"results":users})
    return jsonify(result)


@app.route('/users', methods=['GET'])
def get_all_users():
    raw_users_data = DatabaseHandler.get_all_users()
    users = []
    if raw_users_data:
        for userId, username, email, firstName, lastName, password, roleName, credit, money, cardType, cardNumber, cardHolder, validDate, csc, billingAddress, city, state, zipcode in raw_users_data:
            users.append({"userId": userId, "username": username, "firstName": firstName, "lastName":lastName, "roleName":roleName, "credit":credit, "money":money, "cardType":cardType, "cardNumber":cardNumber, "cardHolder":cardHolder, "validDate":validDate, "csc":csc, "billingAddress":billingAddress, "city":city, "state":state, "zipcode":zipcode})
    result = dict()
    result.update({"results":users})
    return jsonify(result)

@app.route('/bugs', methods=['POST'])
def get_bugs():
    raw_bugs_data = DatabaseHandler.get_bugs(request.data)
    bugs = []
    if raw_bugs_data:
        for bugId, bugName, bugLevel, causingCondition, expectedResult, actualResult, projectId, userId in raw_bugs_data:
            bugs.append({"bugId": bugId, "bugName": bugName, "bugLevel": bugLevel, "causingCondition":causingCondition, "expectedResult":expectedResult, "actualResult":actualResult,"projectId":projectId, "userId":userId})
    result = dict()
    result.update({"results":bugs})
    return jsonify(result)

@app.route('/bugs', methods=['GET'])
def get_all_bugs():
    raw_bugs_data = DatabaseHandler.get_all_bugs()
    bugs = []
    if raw_bugs_data:
        for bugId, bugName, bugLevel, causingCondition, expectedResult, actualResult, projectId, userId in raw_bugs_data:
            bugs.append({"bugId": bugId, "bugName": bugName, "bugLevel": bugLevel, "causingCondition":causingCondition, "expectedResult":expectedResult, "actualResult":actualResult,"projectId":projectId, "userId":userId})
    result = dict()
    result.update({"results":bugs})
    return jsonify(result)

@app.route('/login', methods=['POST'])
def login_user():
    statusCode, message, userId = DatabaseHandler.loginUser(request.data)
    result = dict()
    result['statusCode'] = statusCode
    result['message'] = message
    return jsonify(result)

if __name__ == "__main__":
    app.run()