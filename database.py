from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sqlite.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import User, Prof
    Base.metadata.create_all(bind=engine)
    u = User(b'TLogin', b'TestFirstname', b'TSurname', b'12345', b'admin@localhost')  
    db_session.add(u)  
    db_session.commit()
    p = Prof(b'TestProf', b'TestDescription', b'https://youtu.be/oHg5SJYRHA0', b'http://ya.ru')
    db_session.add(p)  
    db_session.commit()