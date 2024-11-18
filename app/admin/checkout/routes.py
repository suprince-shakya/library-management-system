from app.admin.checkout import bp
from flask_login import login_required
from flask import render_template,request,flash,redirect,url_for
from app.models.book import Book
from app.models.category import Category
from app.models.author import Author
from app.models.user import User
from app.models.book_request import BookRequest,BookRequestStatus
from app.admin.checkout.forms import CheckoutSearchForm
from datetime import datetime
from dateutil.relativedelta import relativedelta
from app.extensions import db
from sqlalchemy import or_
import app

@bp.route('/',methods=['GET'])
@login_required
def index():
  form=CheckoutSearchForm()
  page=request.args.get('page',1,type=int)
  filter=request.args.get('search','',type=str)
  book_requests=BookRequest.query.filter(  
    or_(
      User.firstname.contains(filter),
      User.lastname.contains(filter)
    ),).join(Book).join(User).join(Category).join(Author).order_by(BookRequest.created_at.desc()).paginate(page=page,per_page=7,error_out=False)
  for bookrequest in book_requests.items:
    split=bookrequest.book.picture.split('./app')
    if len(split)>1:
      bookrequest.book.picture=app.Config.APP_HOST + split[1]
    else:
      bookrequest.book.picture=split[0]
  return render_template('dashboard/pages/checkout/index.html',data=book_requests,form=form,url='admin.checkout.index')

@bp.route('/issue/<id>',methods=['GET'])
@login_required
def issue_book(id):
  book_request=BookRequest.query.filter(BookRequest.id==id).first()
  if book_request:
    book_request.issue_date=datetime.today()
    book_request.due_date=datetime.today() + relativedelta(months=1)
    book_request.status=BookRequestStatus.Borrowed.name
    book=Book.query.filter_by(id=book_request.book_id).first()
    book.in_stock = book.in_stock - 1
    db.session.commit()
    flash('Book issued succesfully','success')
    return redirect(url_for('admin.checkout.index'))
  return render_template('dashboard/pages/checkout/index.html')

@bp.route('/return/<id>',methods=['GET'])
@login_required
def return_book(id):
  book_request=BookRequest.query.filter(BookRequest.id==id).first()
  if book_request:
    if book_request.issue_date:
      book_request.returned_date=datetime.today()
      book_request.status=BookRequestStatus.Returned.name
      book=Book.query.filter_by(id=book_request.book_id).first()
      book.in_stock = book.in_stock + 1
      db.session.commit()
      flash('Book returned succesfully','success')
      return redirect(url_for('admin.checkout.index'))
    else:
      flash('Book has not been issued','error')
      return redirect(url_for('admin.checkout.index'))
  return render_template('dashboard/pages/checkout/index.html')

@bp.route('/renew/<id>',methods=['GET'])
@login_required
def renew_book(id):
  book_request=BookRequest.query.filter(BookRequest.id==id).first()
  if book_request:
    if book_request.issue_date:
      if book_request.returned_date:
        book=Book.query.filter_by(id=book_request.book_id).first()
        book.in_stock = book.in_stock - 1
      book_request.issue_date=datetime.today()
      book_request.due_date=datetime.today() + relativedelta(months=1)
      book_request.status=BookRequestStatus.Renewed.name
      book_request.returned_date=None
      db.session.commit()
      flash('Book renewed succesfully','success')
      return redirect(url_for('admin.checkout.index'))
    else:
      flash('Book has not been issued','error')
      return redirect(url_for('admin.checkout.index'))
  return render_template('dashboard/pages/checkout/index.html')

  
