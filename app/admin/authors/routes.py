from app.admin.authors import bp
from flask_login import login_required
from flask import render_template,redirect,url_for,request,flash
from app.admin.authors.forms import AddAuthorForm,AuthorSearchForm,EditAuthorForm
from app.models.author import Author
from app.extensions import db
from sqlalchemy import func

@bp.route('/',methods=['GET'])
@login_required
def index():
  form=AuthorSearchForm()
  page=request.args.get('page',1,type=int)
  filter=request.args.get('search','',type=str)
  authors=Author.query.filter(Author.name.contains(filter)).order_by(Author.created_at.desc()).paginate(page=page,per_page=10,error_out=False)
  return render_template('dashboard/pages/author/index.html',form=form,data=authors,search=filter,url='admin.author.index')

@bp.route('/add',methods=['GET','POST'])
@login_required
def add():
  form=AddAuthorForm()
  if request.method=='POST':
    if form.validate_on_submit():
      author=Author.query.filter(func.lower(Author.name)==func.lower(form.name.data)).first()
      if author:
        flash('Author name already exists','error')
        return redirect(url_for('admin.author.add'))
      else:
        new_author=Author(name=form.name.data)
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for('admin.author.index'))
  return render_template('dashboard/pages/author/add.html',form=form)

@bp.route('/edit/<id>',methods=['GET','POST'])
@login_required
def edit(id):
  form=EditAuthorForm()
  if request.method=='POST':
    if form.validate_on_submit():
      author=Author.query.filter_by(id=id).first()
      if author:
        author.name=form.name.data
        db.session.commit()
        return redirect(url_for('admin.author.index'))
      else:
        flash("Author doesn't exists",'error')
        return redirect(url_for('admin.author.edit'))
      
  author=Author.query.filter_by(id=id).first()
  form.name.data=author.name
  return render_template('dashboard/pages/author/edit.html',form=form)

@bp.route('/delete/<id>',methods=['GET'])
@login_required
def delete(id):
  author=Author.query.filter_by(id=id).first()
  if author:
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('admin.author.index'))
  else:
    flash("Author doesn't exists",'error')
    return redirect(url_for('admin.author.index'))