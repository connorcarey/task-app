from flask import Flask
from flask import Flask, render_template
from firebase import firebase
import firebase_admin
from firebase_admin import firestore, credentials, db

import smtplib, ssl


# Use a service account.
app = Flask(__name__)
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

@app.route('/')
def index():
    db = firestore.client()
    users_ref = db.collection("users").document("Ud8a2ZqK6Ucn9BDm2xuj")

    tasks_ref = users_ref.collection("tasks")
    tasks_docs = tasks_ref.get()

    tasks = [doc.to_dict() for doc in tasks_docs]
    tasks = tasks[0]["deadlineTime"]
    return tasks
    

@app.route('/verify')
def verify():
    return "bo"





def remindEmail(taskID, userID, emailAccount):
    db = firestore.client()
    users_ref = db.collection("users").document(userID)

    name = users_ref.get().to_dict()["name"]

    tasks_ref = users_ref.collection("tasks").document(taskID)
    tasks_docs = tasks_ref.get()

    tasks = [doc.to_dict() for doc in tasks_docs]
    
    title = tasks[0]["taskName"]
    deadline = tasks[0]["deadlineTime"]

    #Email time woo
    port = 587
    smtp_server = "smtp.gmail.com"
    computadora = "itzael.markavion@dealoaks.com"
    reciever = "yhmrt7@gmail.com" #emailAccount here!!
    password = "yamfd6C$"
    message = """\
    Subject: Reminder to complete your task!

    {name}, you have a task to complete! You need to {title} before {deadline}. \n Good luck!""".format(name=name, title=title, deadlineTime=tasks[0]["deadlineTime"])

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo() # Can be omitted
        server.starttls(context=context)
        server.ehlo() # Can be omitted
        server.login(computadora, password)
        server.sendmail(computadora, reciever, message)

