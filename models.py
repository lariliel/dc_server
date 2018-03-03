from sqlalchemy import Column, Integer, String
from database import Base
import bcrypt

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), unique=False)
    surname = Column(String(50), unique=False)
    email = Column(String(120), unique=True)
    password = Column(String(50), unique=False)

    def __init__(self, firstname, surname, password, email=None):
        self.firstname = firstname
        self.surname = surname
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.id)