from db.database import db
from datetime import datetime
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy_utils import UUIDType


class Thread(db.Model):
    __tablename__ = 'threads'
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(255))
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    tag = db.Column(db.String(255))
    sub_tag = db.Column(db.String(255))
    user_id = db.Column(db.String(255),db.ForeignKey("users.id"))
    group = relationship("Group",backref="threads")
    publishted = db.Column(db.Boolean,default=True)
    group_op = db.Column(db.Boolean)
    open_op = db.Column(db.Boolean,default=True)