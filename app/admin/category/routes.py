from app.admin.category import bp
from flask_login import login_required
from flask import render_template,redirect,url_for,request,flash
from app.admin.category.forms import AddCategoryForm,CategorySearchForm,EditCategoryForm
from app.models.category import Category
from app.extensions import db
from sqlalchemy import func

@bp.route('/',methods=['GET'])
@login_required
def index():
  form=CategorySearchForm()
  page=request.args.get('page',1,type=int)
  filter=request.args.get('search','',type=str)
  categories=Category.query.filter(Category.title.contains(filter)).order_by(Category.created_at.desc()).paginate(page=page,per_page=10,error_out=False)
  return render_template('dashboard/pages/category/index.html',form=form,data=categories,search=filter,url='admin.category.index')

@bp.route('/add',methods=['GET','POST'])
@login_required
def add():
  form=AddCategoryForm()
  if request.method=='POST':
    if form.validate_on_submit():
      old_category=Category.query.filter(func.lower(Category.title)==func.lower(form.title.data)).first()
      if old_category:
        flash('Category title already exists','error')
        return redirect(url_for('admin.category.add'))
      else:
        print(form.status.data)
        new_category=Category(title=form.title.data,status=True if form.status.data=='True' else False)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('admin.category.index'))
  return render_template('dashboard/pages/category/add.html',form=form)

@bp.route('/edit/<id>',methods=['GET','POST'])
@login_required
def edit(id):
  form=EditCategoryForm()
  if request.method=='POST':
    if form.validate_on_submit():
      category=Category.query.filter_by(id=id).first()
      if category:
        category.title=form.title.data
        category.status=status=True if form.status.data=='True' else False
        db.session.commit()
        return redirect(url_for('admin.category.index'))
      else:
        flash("Category doesn't already exists",'error')
        return redirect(url_for('admin.category.edit'))
      
  category=Category.query.filter_by(id=id).first()
  form.title.data=category.title
  form.status.data='True' if category.status==True else 'False'
  return render_template('dashboard/pages/category/edit.html',form=form)

@bp.route('/delete/<id>',methods=['GET'])
@login_required
def delete(id):
  category=Category.query.filter_by(id=id).first()
  if category:
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('admin.category.index'))
  else:
    flash("Category doesn't exists",'error')
    return redirect(url_for('admin.category.index'))