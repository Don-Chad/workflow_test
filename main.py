from flask import Flask


app = Flask(__name__)

@app.route('/')
def test_index():
    return 'Hello, world! = this is the updated version, once again. The code is tested and the flask server is updated.'

@app.route('/cow')
def test_cow():
    return 'MOoooOo - thhis also is the fully updated moo!'

https://ucs-blob-store.s3-accelerate.amazonaws.com/blobs/62/fe/1df0-e04e-4749-909a-e799b6acdf49?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA2SBBZFECCYQWRK6G%2F20240615%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240615T134925Z&X-Amz-Expires=3600&X-Amz-Signature=4667db5b9c4017a0af1896674125c843cae98a1d269a208d7d0b867b021cc659&X-Amz-SignedHeaders=host&response-content-disposition=inline%3Bfilename%3D%22file.zip%22%3Bfilename%2A%3DUTF-8%27%27Linux_Unreal_Engine_5.4.2.zip&x-id=GetObject

