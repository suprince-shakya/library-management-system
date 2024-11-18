from app.admin.members import bp
from flask_login import login_required
from flask import render_template,redirect,url_for,request,flash
from app.models.user import User,RolesEnum
from app.admin.members.forms import EditMemberForm,MemberSearchForm
from app.extensions import db
from sqlalchemy import or_

@bp.route('/',methods=['GET'])
@login_required
def index():
  form=MemberSearchForm()
  page=request.args.get('page',1,type=int)
  filter=request.args.get('search','',type=str)
  categories=User.query.filter(
    or_(
      User.firstname.contains(filter),
      User.lastname.contains(filter)
    ),
    User.role==RolesEnum.Customer
  ).order_by(User.created_at.desc()).paginate(page=page,per_page=10,error_out=False)
  return render_template('dashboard/pages/member/index.html',form=form,data=categories,search=filter,url='admin.member.index')

@bp.route('/edit/<id>',methods=['GET','POST'])
@login_required
def edit(id):
  form=EditMemberForm()
  if request.method=='POST':
    if form.validate_on_submit():
      member=User.query.filter_by(id=id).first()
      if member:
        member.firstname=form.firstname.data
        member.lastname=form.lastname.data
        member.status=True if form.status.data=='True' else False
        db.session.commit()
        return redirect(url_for('admin.member.index'))
      else:
        flash("Member doesn't exists",'error')
        return redirect(url_for('admin.member.edit'))
    else:
      print(form.errors)
      
  member=User.query.filter_by(id=id).first()
  form.firstname.data=member.firstname
  form.lastname.data=member.lastname
  form.email.data=member.email
  form.email.render_kw = {'disabled': 'disabled'}
  form.status.data='True' if member.status==True else 'False'
  return render_template('dashboard/pages/member/edit.html',form=form)

@bp.route('/delete/<id>',methods=['GET'])
@login_required
def delete(id):
  member=User.query.filter_by(id=id).first()
  if member:
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('admin.member.index'))
  else:
    flash("Member doesn't exists",'error')
    return redirect(url_for('admin.member.index'))