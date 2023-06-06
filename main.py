
#this is a v3
# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'Hello, world! = this is the updated version, once again. The code is tested and the flask server is updated.'

@app.route('/cow')
def cow():
    return 'MOoooOo - thhis also is the fully updated moo!'


