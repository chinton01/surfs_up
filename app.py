from flask import Flask
app = Flask(__name__)
# @
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/')
def blah():
    return '<h2>Blah is practice</h2>'