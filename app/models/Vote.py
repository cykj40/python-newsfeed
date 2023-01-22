from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey 
from sqlalchemy.orm import relationship

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship("Post", backref="votes")

  
