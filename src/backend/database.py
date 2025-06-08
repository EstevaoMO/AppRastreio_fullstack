from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_BANCO = "sqlite:///./rastreamento.db"

motor = create_engine(URL_BANCO, connect_args={"check_same_thread": False})
SessaoLocal = sessionmaker(autocommit=False, autoflush=False, bind=motor)

Base = declarative_base()

def get_db():
    db = SessaoLocal()
    try:
        yield db
    finally:
        db.close()