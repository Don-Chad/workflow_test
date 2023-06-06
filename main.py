from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world! = this is the updated version, once again. The code is tested and the flask server is updated.'

@app.route('/cow')
def cow():
    return 'MOoooOo - thhis also is the fully updated moo!'

def test_index():
    response = requests.get('http://localhost:5000/')
    assert response.status_code == 200
    assert 'Hello, world!' in response.text

def test_cow():
    response = requests.get('http://localhost:5000/cow')
    assert response.status_code == 200
    assert 'MOoooOo' in response.text
