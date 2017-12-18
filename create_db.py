from sqlalchemy import create_engine
from models import Base
from os import getenv

engine = create_engine(getenv('DATABASE_URI'))

if __name__ == '__main__':
    Base.metadata.create_all(engine)
