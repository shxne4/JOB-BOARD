from .user import create_user
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    # create_user(id='1', username='shane', email='mail.com', phone='1234567', person='jobseeker')
