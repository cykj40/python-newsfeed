from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt 
from sqlalchemy import orm


salt = bcrypt.gensalt()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    _password = Column(String(100), nullable=False)
    salt = bcrypt.gensalt()
    
    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email
        return email

    @validates('password')
    def validate_password(self, key, password):
        assert len(password) >= 8
        self._password = bcrypt.hashpw(password.encode('utf-8'), self.salt)

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self._password.encode('utf-8'))

    @orm.column_property
    def password(self):
        return self._password




