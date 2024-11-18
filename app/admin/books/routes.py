from app.admin.books import bp
from flask_login import login_required
from flask import render_template,redirect,url_for,request,flash
from app.admin.books.forms import AddBookForm,BookSearchForm,EditBookForm
from app.models.book import Book
from app.models.category import Category
from app.models.author import Author
from app.extensions import db
from os import path,unlink
from werkzeug.utils import secure_filename
import app

@bp.route('/',methods=['GET'])
@login_required
def index():
  form=BookSearchForm()
  page=request.args.get('page',1,type=int)
  filter=request.args.get('search','',type=str)
  books=Book.query.filter(Book.name.contains(filter)).join(Category).join(Author).order_by(Book.created_at.desc()).paginate(page=page,per_page=7,error_out=False)
  for book in books.items:
    split=book.picture.split('./app')
    book.picture=app.Config.APP_HOST + split[1]
  return render_template('dashboard/pages/book/index.html',form=form,data=books,search=filter,url='admin.book.index')

@bp.route('/add',methods=['GET','POST'])
@login_required
def add():
  form=AddBookForm()
  if request.method=='POST':
    if form.validate_on_submit():
      filename = secure_filename(form.picture.data.filename)
      file_path = path.join('./app/static/uploads/', filename)
      form.picture.data.save(file_path)
      new_book=Book(name=form.name.data,category_id=form.category_id.data,author_id=form.author_id.data,isbn=form.isbn.data,quantity=form.quantity.data,in_stock=form.quantity.data,price=form.price.data,description=form.description.data,picture=file_path)
      db.session.add(new_book)
      db.session.commit()
      return redirect(url_for('admin.book.index'))
  categories=Category.query.filter(Category.status==True).all();
  authors=Author.query.all();
  category_choices=list(map((lambda x : (x.id,x.title)),categories))
  author_choices=list(map((lambda x : (x.id,x.name)),authors))
  form.category_id.choices=category_choices
  form.author_id.choices=author_choices
  return render_template('dashboard/pages/book/add.html',form=form)

@bp.route('/edit/<id>',methods=['GET','POST'])
@login_required
def edit(id):
  form=EditBookForm()
  if request.method=='POST':
    if form.validate_on_submit():
      book=Book.query.filter_by(id=id).first()
      if book:
        if form.picture.data:
          try:
            unlink(book.picture)
          except:
            print('Error removing file')
          filename = secure_filename(form.picture.data.filename)
          file_path = path.join('./app/static/uploads/', filename)
          form.picture.data.save(file_path)
          book.picture=file_path

        book.name=form.name.data
        book.category_id=form.category_id.data
        book.author_id=form.author_id.data
        book.isbn=form.isbn.data
        book.quantity=form.quantity.data
        book.price=form.price.data
        book.description=form.description.data
     
        db.session.commit()
        return redirect(url_for('admin.book.index'))
      else:
        flash("Book doesn't exists",'error')
        return redirect(url_for('admin.book.edit'))
    else:
      print(form.errors)
  book=Book.query.filter_by(id=id).join(Category).join(Author).first()    
  categories=Category.query.filter(Category.status==True).all();
  authors=Author.query.all();
  category_choices=list(map((lambda x : (x.id,x.title)),categories))
  author_choices=list(map((lambda x : (x.id,x.name)),authors))
  form.category_id.choices=category_choices
  form.category_id.data=book.category_id
  form.author_id.choices=author_choices    
  form.author_id.data=book.author_id    
  form.name.data=book.name
  form.quantity.data=book.quantity
  form.price.data=book.price
  form.picture.data=book.picture
  form.isbn.data=book.isbn
  form.description.data=book.description
  return render_template('dashboard/pages/book/edit.html',form=form)

@bp.route('/delete/<id>',methods=['GET'])
@login_required
def delete(id):
  book=Book.query.filter_by(id=id).first()
  if book:
    try:
      unlink(book.picture)
    except:
      print('No picture')
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('admin.book.index'))
  else:
    flash("Book doesn't exists",'error')
    return redirect(url_for('admin.book.index'))
  
