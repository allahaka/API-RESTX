from core.db.main import db
from core.db.models import Users


def select_all_users():
    return db.query(Users).all()


def select_user_by_id(user_id):
    return db.query(Users).filter(Users.id == user_id).first()
