from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Not here'

@app.route('/api/0.1')
def index():
    return '<a href="https://github.com/lariliel/dc_server">https://github.com/lariliel/dc_server</a>'