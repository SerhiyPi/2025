from smtplib import SMTPResponseException
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import _SessionClassMethods

 
SQLALCHEMY_DATABASE_URL = 'sqlite:///./Together.db'
 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
 
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

 
Base = declarative_base()
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)
