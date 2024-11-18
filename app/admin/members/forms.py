from wtforms import StringField,SubmitField,RadioField,SearchField,EmailField
from wtforms.validators import InputRequired,Length
from flask_wtf import FlaskForm

class MemberSearchForm(FlaskForm):
  search=SearchField(render_kw={"placeholder": "Search Members"})

class EditMemberForm(FlaskForm):
  firstname= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"Firstname"})
  lastname= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"Lastname"})
  email= EmailField(render_kw={"placeholder":"Email"})
  status= RadioField('Status',choices=[(True,'Enable'),(False,'Disable')])
  submit=SubmitField("Edit Member")