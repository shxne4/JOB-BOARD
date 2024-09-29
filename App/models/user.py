from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.Integer(7), nullable=False)

    def __init__(self, username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
            'email': self.email
            'phone': self.phone
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

