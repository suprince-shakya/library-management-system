from app.models.base import BaseTable
from app.extensions import db
from flask_login import UserMixin
from app.models.user import User
from app.models.book import Book
import enum

class BookRequestStatus(enum.Enum):
  Requested = 'requested'
  Borrowed = 'borrowed'
  Renewed = 'renewed'
  Returned = 'returned'

class BookRequest(BaseTable,UserMixin):
  __tablename__='book_requests'
  id=db.Column(db.Integer,primary_key=True)
  user_id=db.Column(db.Integer,db.ForeignKey(User.id,ondelete='CASCADE'))
  book_id=db.Column(db.Integer,db.ForeignKey(Book.id,ondelete='CASCADE'))
  issue_date=db.Column(db.DateTime(timezone=True),nullable=True)
  due_date=db.Column(db.DateTime(timezone=True),nullable=True)
  returned_date=db.Column(db.DateTime(timezone=True),nullable=True)
  fine=db.Column(db.Float(precision=2),nullable=True)
  status=db.Column(db.Enum(BookRequestStatus),default='Requested')

  user = db.relationship(User, foreign_keys='BookRequest.user_id')
  book = db.relationship(Book, foreign_keys='BookRequest.book_id')


