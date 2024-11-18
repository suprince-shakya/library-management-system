from app.models.base import BaseTable
from app.extensions import db
from flask_login import UserMixin

class Author(BaseTable,UserMixin):
  __tablename__='authors'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(20),nullable=False)