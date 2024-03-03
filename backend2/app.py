from flask import Flask, render_template, request, redirect, session
from firebase import firebase
import firebase_admin
from firebase_admin import firestore, credentials, db

from email.mime.text import MIMEText
import smtplib, ssl
from datetime import datetime

# Use a service account.
app = Flask(__name__)
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

@app.route('/api')
def index():
    return getTasks("", "Ud8a2ZqK6Ucn9BDm2xuj")
    
@app.route('/api/dashboard', method=["GET"])
def dashboard():
    return getTasks("", session['userID'])

# add task, accept invite, send proof (return media), confirm

@app.route('/api/othersTasks', method=['GET', 'POST'])
def othersTasks():
    if request.method == 'GET':
        return 
    if request.method == 'POST':
        request_data = request.get_json()
        if request_data:
            request_data = request_data.to_dict()



@app.route('/api/login', method=["GET", "POST"])
def login():
    if request.method == "POST":
        request_data = request.get_json()
        if request_data:
            if 'userID' in request_data:
                session['userID'] = request_data['userID']
    

@app.route('/api/makeTask', method=['POST'])
def makeTask():
    taskName = request.form.get('taskName')
    taskDescription = request.form.get('taskDescription')
    recieverID = request.form.get('recieverID')
    start = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    deadline = request.form.get('deadlineTime')
    duration = request.form.get("duration")

    personalTask = {
        "completed" : False,
        "confirmationURL" : "",
        "confirmerID" : "",
        "deadline" : deadline,
        "duration" : duration,
        "start": start,
        "taskDescription": taskDescription,
        "taskName": taskName,
        "verified" : False,        
    }

    otherTask = {
        ""
    }
    




def remindEmail(taskID, userID, emailAccount):
    #Get the task information
    info = getTasks(taskID, userID)

    db = firestore.client()
    specificUser = db.collection("users").document(userID).get().to_dict()
    
    name = specificUser[0]["name"]
    timeToComplete = timeLeft(taskID, userID)
    nameOfTask = info[0]["taskName"]

    msg_body = "Hi " + name + ",\n\nYou have " + str(int(timeToComplete / 60)) + " hour(s) left to " + nameOfTask + "!\n\nFrom,\nDouble Check"
    msg = MIMEText(msg_body)
    msg['Subject'] = 'Reminder: ' + nameOfTask + ' is due soon!'
    msg['From'] = 'john.tanaristy@gmail.com'
    msg['To'] = emailAccount 

    server = 'localhost'
    portNum = 25
    # password = '' 

    # Send the email
    with smtplib.SMTP(server, portNum) as server:
        server.sendmail(msg['From'], msg['To'], msg.as_string())
  
    

def getTasks(taskID, userID):
    db = firestore.client()
    allUsers = db.collection("users").document(userID)

    if taskID == "":
        allTasks = allUsers.collection("tasks").stream()
        #tasks_docs = allTasks.get()
        tasks = [doc.to_dict() for doc in allTasks]
    else:
        tasks = allUsers.collection("tasks").document(taskID).get().to_dict()
    return tasks


def getAnnoyanceLevel(taskID, userID):
    info = getTasks(taskID, userID)
    
    howLongItTakes = info[0]["duration"] * 60
    startTime = info[0]["startTime"]
    endTime = datetime.now().strftime("%Y-%M-%D %H:%M:%S")

    timeLeft = diffTime(startTime, endTime)

    level = min(int(timeLeft / howLongItTakes), 4)
    return level    

#Difference in two times in minutes
def diffTime(t1, t2):
    startingTime = datetime.strptime(t1, '%Y-%M-%D %H:%M:%S')
    endingTime = datetime.strptime(t2, '%Y-%M-%D %H:%M:%S')

    #Convert strings back to time to find the difference
    timeLeft = endingTime - startingTime

    #Don't really care about seconds tbh
    timeLeft = round(timeLeft.total_seconds() / 60)
    return timeLeft

#Get the time remaining for a task
def timeLeft(taskID, userID):
    info = getTasks(taskID, userID)

    #Get the current time
    curTime = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    deadline = info[0]["deadlineTime"]

    return diffTime(curTime, deadline)


