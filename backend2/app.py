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
    ref = db.reference('/users/Ud8a2ZqK6Ucn9BDm2xuj/tasks/yP2sOyfpsXJvcu9lG4zj')
    # db = firestore.client()
    # users_ref = db.collection("users")
    # docs = users_ref.get()
    wow = ref.get()
    
    # return [doc.to_dict() for doc in docs]
    return wow