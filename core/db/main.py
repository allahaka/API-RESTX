from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.consts import DATABASE_URI
from core.db.models import Base


engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

db = Session()

Base.metadata.create_all(engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
