from db.database import db
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy_utils import UUIDType


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    groupauth = db.Column(db.Boolean,default=False)
    threads = relationship("Thread",backref="users")
    comment = relationship("Comment",backref="users")
    groups = relationship("Group",backref="users")