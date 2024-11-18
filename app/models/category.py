from app.models.base import BaseTable
from app.extensions import db
from flask_login import UserMixin

class Category(BaseTable,UserMixin):
  __tablename__='categories'
  id=db.Column(db.Integer,primary_key=True)
  title=db.Column(db.String(20),nullable=False)
  status=db.Column(db.Boolean,nullable=False)