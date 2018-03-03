# dc_server
# сборка пакетов
sudo pip3 install virtualenv  
virtualenv venv  
. venv/bin/activate  
pip install Flask  
pip install Flask-SQLAlchemy  
pip install bcrypt  

<h1>Запуск</h1>
FLASK_APP=server.py FLASK_DEBUG=1 flask run --host=0.0.0.0  
<h1>Адреса</h1>
/api/0.1/users/$id  
/api/0.1/users/login  
