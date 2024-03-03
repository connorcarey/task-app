from flask import Flask, render_template, request, redirect, session
from firebase import firebase
import firebase_admin
from firebase_admin import firestore, credentials, db

import smtplib, ssl
from datetime import datetime

# Use a service account.
app = Flask(__name__)
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

@app.route('/api')
def index():
    return getTasks("", "Ud8a2ZqK6Ucn9BDm2xuj")
    
@app.route('/api/dashboard', method=["GET", "POST"])
def dashboard():
    if request.method == "GET":
        #do stuff
        return 
    elif request.method == "POST":
        #do stuff

# add task, accept invite, send proof (return media), confirm

@app.route('/api/verify')
def verify():
    return "bo"

@app.route('/api/login', method=["GET", "POST"])
def login():
    






def remindEmail(taskID, userID, emailAccount):
    #Get the task information
    info = getTasks(taskID, userID)

    db = firestore.client()
    specificUser = db.collection("users").document(userID).get().to_dict()
    
    name = specificUser[0]["name"]
    timeToComplete = timeLeft(taskID, userID)
    nameOfTask = specificUser[0]["taskName"]

    msg = "Hi " + name + ",\n\nYou have " + (int)(timeToComplete / 60) + " hour(s) left to " + nameOfTask + "!"
    msg = msg + "\n\nFrom,\nDouble Check"

    #Email "msg" to emailAccount
    

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


