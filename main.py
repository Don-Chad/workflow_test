# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'Hello, world! = this is the updated version.'

@app.route('/cow')
def cow():
    return 'MOoooOo - thhis is the fully updated moo!'

#this is a v2