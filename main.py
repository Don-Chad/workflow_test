from flask import Flask


app = Flask(__name__)

@app.route('/')
def test_index():
    return 'Hello, world! = this is the updated version, once again. The code is tested and the flask server is updated.'

@app.route('/cow')
def test_cow():
    return 'MOoooOo - thhis also is the fully updated moo!'


