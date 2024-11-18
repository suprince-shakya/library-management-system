from app.models.base import BaseTable
from app.extensions import db
from flask_login import UserMixin
from app.models.category import Category
from app.models.author import Author

class Book(BaseTable,UserMixin):
  __tablename__='books'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(255),nullable=False)
  category_id=db.Column(db.Integer,db.ForeignKey(Category.id,ondelete='SET NULL'))
  author_id=db.Column(db.Integer,db.ForeignKey(Author.id,ondelete='SET NULL'))
  isbn=db.Column(db.Integer,nullable=False)
  quantity=db.Column(db.Integer,nullable=False)
  price=db.Column(db.Float(precision=2),nullable=False)
  picture=db.Column(db.String(200),nullable=False)
  description=db.Column(db.Text,nullable=True)
  in_stock=db.Column(db.Integer,nullable=False)

  category = db.relationship(Category, foreign_keys='Book.category_id')
  author = db.relationship(Author, foreign_keys='Book.author_id')


