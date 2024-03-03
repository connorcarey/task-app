from flask import Flask
from flask import Flask, render_template
from firebase import firebase
import firebase_admin
from firebase_admin import firestore, credentials, db



# Use a service account.
app = Flask(__name__)
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

@app.route('/')
def hello():    
    
    db = firestore.client()
    users_ref = db.collection("users").document("Ud8a2ZqK6Ucn9BDm2xuj")

    tasks_ref = users_ref.collection("tasks")
    tasks_docs = tasks_ref.get()

    tasks = [doc.to_dict() for doc in tasks_docs]
    return tasks