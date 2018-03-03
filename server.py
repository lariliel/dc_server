from flask import Flask
app = Flask(__name__)

from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    return 'Not here'

@app.route('/api/0.1')
def apiIndex():
    return '<a href="https://github.com/lariliel/dc_server">https://github.com/lariliel/dc_server</a>'