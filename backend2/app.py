from flask import Flask
import firebase_admin
from firebase_admin import credentials
from firebase import firebase
from firebase_admin import db
from flask import Flask, render_template


#cred = credentials.Certificate("C:\Users\yhmrt\OneDrive\Documents\GitHub\task-app\backend2\task-app-b58f4-firebase-adminsdk-2pkh6-ff0bf43edd.json")
#firebase_admin.initialize_app(cred)
#ref = db.reference("/")
firebase = firebase.FirebaseApplication('https://task-app.nam5.firebasedatabase.app', None)


app = Flask(__name__)


@app.route('/')
def hello():
    result = firebase.get('/tasks', None)
    return str(result)