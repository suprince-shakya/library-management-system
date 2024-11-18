from app.models.base import BaseTable
from app.extensions import db
from flask_login import UserMixin
import enum

class RolesEnum(enum.Enum):
  Admin = 'admin'
  Customer = 'customer'

class User(BaseTable,UserMixin):
  __tablename__='users'
  id=db.Column(db.Integer,primary_key=True)
  firstname=db.Column(db.String(20),nullable=False)
  lastname=db.Column(db.String(20),nullable=False)
  email=db.Column(db.String(50),nullable=False,unique=True)
  password=db.Column(db.String(80),nullable=False)
  status=db.Column(db.Boolean,nullable=False,default=True)
  role=db.Column(db.Enum(RolesEnum),default='Customer')