from app.admin import bp
from flask_login import login_required,current_user
from flask import render_template,redirect,url_for,request,flash
from app.models.book import Book
from app.models.user import User,RolesEnum
from app.models.category import Category
from app.models.author import Author
from app.models.book_request import BookRequest,BookRequestStatus
from app.admin.forms import ChangePasswordForm
from app.extensions import db
from sqlalchemy import func
from app.extensions import db,bcrypt
import app

@bp.route('/',methods=['GET'])
@login_required
def dashboard():
  total_books_count=Book.query.count()
  total_borrowed_books_count=BookRequest.query.filter(BookRequest.status==BookRequestStatus.Borrowed.name).count()
  total_returned_books_count=BookRequest.query.filter(BookRequest.status==BookRequestStatus.Returned.name).count()
  total_active_members_count=User.query.filter(User.status==True,User.role==RolesEnum.Customer.name).count()
  total_blocked_members_count=User.query.filter(User.status==False,User.role==RolesEnum.Customer.name).count()
  total_recently_checkouts= BookRequest.query.filter(BookRequest.status==BookRequestStatus.Borrowed.name).join(User).join(Book).join(Author).join(Category).limit(3)
  top_books=db.session.query(Book,Author.name,Category.title,func.count(BookRequest.book_id).label('total_requests')).join(BookRequest).join(Author).join(Category).group_by(Book,Author.name,Category.title).order_by(func.count(BookRequest.book_id).desc()).limit(3).all()
  total_recent_member=User.query.filter(User.status==True,User.role==RolesEnum.Customer.name).order_by(User.created_at.desc()).limit(4)
  for data in top_books:
    split=data[0].picture.split('./app')
    if len(split)>1:
      data[0].picture=app.Config.APP_HOST + split[1]
    else:
      data[0].picture=split[0]
  for recently_checkout in total_recently_checkouts:
    split=recently_checkout.book.picture.split('./app')
    if len(split)>1:
      recently_checkout.book.picture=app.Config.APP_HOST + split[1]
    else:
      recently_checkout.book.picture=split[0]
  stats=dict(total_books=total_books_count,total_borrowed_books=total_borrowed_books_count,total_active_members=total_active_members_count,total_blocked_members=total_blocked_members_count,total_returned_books=total_returned_books_count,recently_checkouts=total_recently_checkouts,top_books=top_books,recent_members=total_recent_member)
  return render_template('dashboard/index.html',data=stats)

@bp.route('/change-password',methods=['GET','POST'])
@login_required
def change_password():
  form=ChangePasswordForm()
  if request.method == 'POST':
    if form.validate_on_submit():
      user=User.query.filter_by(id=current_user.id).first()
      if bcrypt.check_password_hash(user.password,form.current_pass.data):
        if form.new_pass.data==form.confirm_pass.data:
          hashed_password=bcrypt.generate_password_hash(form.new_pass.data)
          user.password=hashed_password
          db.session.commit()
          flash("Password updated succesfully","success")
          return redirect(url_for('admin.change_password'))
        else:
          flash("New password and confirm password doesn't match","error")
          return redirect(url_for('admin.change_password'))
      else:
        flash("Current password doesn't match","error")
        return redirect(url_for('admin.change_password'))
  return render_template('dashboard/change-password.html',form=form)

# Registered sub blueprint(modules)
from app.admin.members import bp as member_bp
bp.register_blueprint(member_bp, url_prefix="/member")

from app.admin.books import bp as book_bp
bp.register_blueprint(book_bp, url_prefix="/book")

from app.admin.category import bp as category_bp
bp.register_blueprint(category_bp, url_prefix="/category")

from app.admin.authors import bp as author_bp
bp.register_blueprint(author_bp, url_prefix="/author")

from app.admin.checkout import bp as checkout_bp
bp.register_blueprint(checkout_bp, url_prefix="/checkout")