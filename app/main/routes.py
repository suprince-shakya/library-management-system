from flask import render_template,redirect,url_for,request,flash
from app.main import bp
from flask_login import login_user,logout_user,login_required,current_user
from app.models.user import User,RolesEnum
from app.models.book import Book
from app.models.category import Category
from app.models.author import Author
from app.extensions import db,bcrypt,login_manager
from app.models.book_request import BookRequest,BookRequestStatus
from app.main.forms import BookSearchForm,ChangePasswordForm,RegisterForm,LoginForm,EditProfileForm
from datetime import datetime
import app

@bp.route('/health-check')
def healthCheck():
  data={'msg':'Application running successfully'}
  return data,200

@bp.route('/')
def index():
  loggedInUser=False
  if current_user.is_authenticated:
    loggedInUser=True
  books=db.session.query(Book).order_by(Book.created_at.desc()).join(Category).join(Author).limit(5)
  for book in books:
    split=book.picture.split('./app')
    book.picture=app.Config.APP_HOST + split[1]
  return render_template('index.html',data=books,loggedInUser=loggedInUser)

@bp.route('/books')
def book():
  form=BookSearchForm()
  filter=request.args.get('search','',type=str)
  page=request.args.get('page',1,type=int)
  loggedInUser=False
  if current_user.is_authenticated:
    loggedInUser=True
  books=Book.query.filter(Book.name.contains(filter)).join(Category).join(Author).paginate(page=page,per_page=15,error_out=False)
  for book in books:
    split=book.picture.split('./app')
    book.picture=app.Config.APP_HOST + split[1]
  return render_template('book.html',data=books,form=form,loggedInUser=loggedInUser,url='main.book')

@bp.route('/books/<id>/request',methods=['GET'])
@login_required
def book_request(id):
  if current_user.status==False:
    flash('Your account has been disabled. Please contact admin.','error')
    return redirect(url_for('main.single_book',id=id))
  book=Book.query.filter_by(id=id).first()
  if book:
    old_book_request=BookRequest.query.filter(BookRequest.book_id==id,BookRequest.user_id==current_user.id).first()
    if old_book_request:
      flash('You have already requested for this book','error')
      return redirect(url_for('main.single_book',id=id))
    else:
      new_book_request=BookRequest(user_id=current_user.id,book_id=id)
      db.session.add(new_book_request)
      db.session.commit()
      flash('You have sucessfully requested for this book','success')
      return redirect(url_for('main.single_book',id=id))
  flash('No book found','error')
  return redirect(url_for('main.single_book',id=id))

@bp.route('/books/<id>')
def single_book(id):
  loggedInUser=False
  alreadyRequestedBook=False
  if current_user.is_authenticated:
    loggedInUser=True
    book_request=BookRequest.query.filter(BookRequest.book_id==id,BookRequest.user_id==current_user.id).first()
    if book_request:
      alreadyRequestedBook=True
  book=Book.query.filter_by(id=id).join(Category).join(Author).first()
  split=book.picture.split('./app')
  book.picture=app.Config.APP_HOST + split[1]
  return render_template('book-detail.html',data=book,loggedInUser=loggedInUser,alreadyRequestedBook=alreadyRequestedBook)

@bp.route('/login',methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    if current_user.role.name==RolesEnum.Admin.name:
      return redirect(url_for('admin.dashboard'))
    else:
      return redirect(url_for('main.dashboard'))
  loginForm =LoginForm()
  if request.method == 'POST':
    if loginForm.validate_on_submit():
      user=User.query.filter_by(email=loginForm.email.data).first()
      if user and bcrypt.check_password_hash(user.password,loginForm.password.data):
        if user.role.name==RolesEnum.Admin.name:
          login_user(user)
          return redirect(url_for('admin.dashboard'))
        else:
          login_user(user)
          return redirect(url_for('main.dashboard'))
      else:
        flash('Invalid Credentials','error')
        return redirect(url_for('main.login'))
  return render_template('login.html',form=loginForm)

@bp.route('/dashboard',methods=['GET'])
@login_required
def dashboard():
  total_book_requested_count=BookRequest.query.filter(BookRequest.user_id==current_user.id).count()
  total_book_returned_count=BookRequest.query.filter(BookRequest.user_id==current_user.id,BookRequest.status==BookRequestStatus.Returned.name).count()
  total_book_issued_count=BookRequest.query.filter(BookRequest.user_id==current_user.id,BookRequest.status==BookRequestStatus.Borrowed.name).count()
  total_book_issued_all=BookRequest.query.filter(BookRequest.user_id==current_user.id,BookRequest.status==BookRequestStatus.Borrowed.name).all()
  total_recent_book_issued=BookRequest.query.filter(BookRequest.user_id==current_user.id,BookRequest.status==BookRequestStatus.Borrowed.name).join(Book).join(Category).order_by(BookRequest.created_at).limit(3)
  total_book_not_returned=0
  for bookrequest in total_book_issued_all:
    if bookrequest.due_date:
      future=datetime.strptime(bookrequest.due_date.strftime('%d/%m/%Y'),"%d/%m/%Y")
      present=datetime.now()
      if present.date() > future.date():
        total_book_not_returned += 1
  for recentbook in total_recent_book_issued:
    split=recentbook.book.picture.split('./app')
    recentbook.book.picture=app.Config.APP_HOST + split[1]
  stats=dict(total_book_requested=total_book_requested_count,total_book_returned=total_book_returned_count,total_book_issued=total_book_issued_count,total_book_not_returned=total_book_not_returned,recent_books=total_recent_book_issued)
  return render_template('dashboard.html',data=stats)

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
          return redirect(url_for('main.change_password'))
        else:
          flash("New password and confirm password doesn't match","error")
          return redirect(url_for('main.change_password'))
      else:
        flash("Current password doesn't match","error")
        return redirect(url_for('main.change_password'))
  return render_template('change-password.html',form=form)

@bp.route('/book-request',methods=['GET'])
@login_required
def request_book():
  page=request.args.get('page',1,type=int)
  user_id=current_user.id
  book_requests=BookRequest.query.filter(BookRequest.user_id==user_id).order_by(BookRequest.created_at.desc()).join(Book).join(Category).join(Author).paginate(page=page,per_page=4,error_out=False)
  for book_request in book_requests:
    split=book_request.book.picture.split('./app')
    book_request.book.picture=app.Config.APP_HOST + split[1]
  return render_template('book-request.html',data=book_requests,url='main.request_book')

@bp.route('/my-profile',methods=['GET','POST'])
@login_required
def profile():
  form=EditProfileForm()
  if request.method=='POST':
    if form.validate_on_submit():
      user=User.query.filter_by(id=current_user.id).first()
      if user:
        user.firstname=form.firstname.data
        user.lastname=form.lastname.data
        db.session.commit()
        flash("User profile updated succesfully",'success')
        return redirect(url_for('main.profile'))
      else:
        flash("User doesn't exists",'error')
        return redirect(url_for('main.profile'))
  user=User.query.filter_by(id=current_user.id).first()
  form.firstname.data=user.firstname
  form.lastname.data=user.lastname
  form.email.data=user.email
  form.email.render_kw = {'disabled': 'disabled'}
  return render_template('my-profile.html',form=form,data=user)

@bp.route('/signup',methods=['GET','POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('admin.dashboard'))
  
  form =RegisterForm()
  if request.method == 'POST':
    if form.validate_on_submit():
      hashed_password=bcrypt.generate_password_hash(form.password.data)
      new_user=User(firstname=form.firstname.data,lastname=form.lastname.data,email=form.email.data,password=hashed_password)
      db.session.add(new_user)
      db.session.commit()
      return redirect(url_for('main.login'))
  loggedInUser=False
  if current_user.is_authenticated:
    loggedInUser=True
  return render_template('register.html',form=form,loggedInUser=loggedInUser)

@bp.route('/logout',methods=['GET'])
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized_callback():
  return redirect(url_for('main.login'))