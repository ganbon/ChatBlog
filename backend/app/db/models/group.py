from db.database import db
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy_utils import UUIDType


class Group(db.Model):
    __tablename__ = "group"
    rootuser_id = db.Column(UUIDType(binary=False),db.ForeignKey("users.id"), primary_key=True)
    group_id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100),primary_key=True)