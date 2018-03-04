# dc_server
# сборка пакетов
sudo pip3 install virtualenv  
virtualenv venv  
. venv/bin/activate  
pip install Flask  
pip install Flask-SQLAlchemy  
pip install bcrypt  

# Создание БД  
FLASK_APP=server.py flask shell  
from database import init_db  
init_db()  
  
from database import db_session  
from models import User  
u = User(b'TLogin', b'TestFirstname', b'TSurname', b'12345', b'admin@localhost')  
db_session.add(u)  
db_session.commit()  
User.query.all()  
exit()  
  
# Запуск  
FLASK_APP=server.py FLASK_DEBUG=1 flask run --host=0.0.0.0  

# Адреса  
/api/0.1/users/add POST  
/api/0.1/users/$id GET  
/api/0.1/users/$id PUT  
/api/0.1/users/$id/vacancies GET  
/api/0.1/prof  
/api/0.1/prof/add  
/api/0.1/prof/$id  
/api/0.1/prof/$id/update  
/api/0.1/prof/$id/delete  
/api/0.1/prof/$id/getVacancies  
/api/0.1/company  
/api/0.1/company/add  
/api/0.1/company/$id  
/api/0.1/company/$id/update  
/api/0.1/company/$id/delete  
/api/0.1/company/$id/enable  
/api/0.1/company/$id/disable  
/api/0.1/company/$id/getVacancies  