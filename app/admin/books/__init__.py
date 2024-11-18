from flask import Blueprint
from app.models.book import Book
from app.extensions import db

bp=Blueprint('book',__name__)

@bp.cli.command('syncstock')
def sync_stock():
  books=Book.query.all()
  for book in books:
    book.in_stock=book.quantity
    db.session.commit()


from app.admin.books import routes