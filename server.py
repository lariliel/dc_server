from flask import Flask, jsonify, request
app = Flask(__name__)

from database import db_session
from models import User, Prof

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    return 'Not here'

@app.route('/api/0.1')
def apiIndex():
    return '<a href="https://github.com/lariliel/dc_server">https://github.com/lariliel/dc_server</a>'

@app.route('/api/0.1/users/<int:user_id>', methods=['GET', 'PUT'])
def getUserJSONById(user_id=None):
    user = User.query.filter(User.id == user_id).first()
    if request.method == 'GET':
        return jsonify({'id': user.id, 'firstname': user.firstname.decode('utf-8'), 'surname': user.surname.decode('utf-8'), 'login': user.login.decode('utf-8')})
    if request.method == 'PUT':
        try:
            user.login = request.form['login']
            user.firstname = request.form['firstname']
            user.surname = request.form['surname']
            user.email = request.form['email']
            user.password = bcrypt.hashpw(request.form['password'], bcrypt.gensalt())
            db_session.update(user)  
            db_session.commit()
        except Exception as e:
            return jsonify({'status': 0, 'message': repr(e)})
        return jsonify({'status': 1, 'id': user.id, 'firstname': user.firstname.decode('utf-8'), 'surname': user.surname.decode('utf-8'), 'login': user.login.decode('utf-8')})

@app.route('/api/0.1/users/add', methods=['POST'])
def addUser():
    result = {'status': 0, 'message': 'Error'}
    try:
        u = User(request.form['login'], request.form['firstname'], request.form['surname'], request.form['password'], request.form['email'])
        db_session.add(u)  
        db_session.commit()
        result = {'status': 1, 'message': "Пользователь успешно добавлен"}
    except Exception as e:
        result = {'status': 0, 'message': repr(e)}
    return jsonify(result)

@app.route('/api/0.1/profs', methods=['GET'])
def getProfJSONLists():
    profs = Prof.query.all()
    result = []
    for prof in profs:
        result.append(prof.prof_id)
    return jsonify(result)

@app.route('/api/0.1/profs/<int:prof_id>', methods=['GET', 'PUT'])
def getProfJSONById(prof_id=None):
    prof = Prof.query.filter(Prof.prof_id == prof_id).first()
    if request.method == 'GET':
        return jsonify({'prof_id': prof.prof_id, 'name': prof.name.decode('utf-8'), 'description': prof.description.decode('utf-8'), 'videourl': prof.videourl.decode('utf-8'), 'descurl': prof.descurl.decode('utf-8')})
    if request.method == 'PUT':
        try:
            prof.login = request.form['login']
            prof.firstname = request.form['firstname']
            prof.surname = request.form['surname']
            prof.email = request.form['email']
            prof.password = bcrypt.hashpw(request.form['password'], bcrypt.gensalt())
            db_session.update(prof)  
            db_session.commit()
        except Exception as e:
            return jsonify({'status': 0, 'message': repr(e)})
        return jsonify({'status': 0, 'prof_id': prof.prof_id, 'name': prof.name.decode('utf-8'), 'description': prof.description.decode('utf-8'), 'videourl': prof.videourl.decode('utf-8'), 'descurl': prof.descurl.decode('utf-8')})

@app.route('/api/0.1/profs/add', methods=['POST'])
def addProf():
    result = {'status': 0, 'message': 'todo'}
    return jsonify(result)
    try:
        u = User(request.form['login'], request.form['firstname'], request.form['surname'], request.form['password'], request.form['email'])
        db_session.add(u)  
        db_session.commit()
        result = {'status': 1, 'message': "Пользователь успешно добавлен"}
    except Exception as e:
        result = {'status': 0, 'message': repr(e)}
    return jsonify(result)