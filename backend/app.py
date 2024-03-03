from flask import Flask
import firebase_admin
from firebase_admin import credentials
from firebase import firebase
from firebase_admin import db
from flask import Flask, render_template


cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
ref = db.reference("/")
firebase = firebase.FirebaseApplication('https://task-app.nam5.firebasedatabase.app', None)


app = Flask(__name__)


@app.route('/')
def hello():
    result = firebase.get('/tasks', None)
    return str(result)