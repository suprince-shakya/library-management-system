from wtforms import StringField,SubmitField,RadioField,SearchField
from wtforms.validators import InputRequired,Length
from flask_wtf import FlaskForm

class AuthorSearchForm(FlaskForm):
  search=SearchField(render_kw={"placeholder": "Search Author"})

class AddAuthorForm(FlaskForm):
  name= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"Name"})
  submit=SubmitField("Add Author")

class EditAuthorForm(FlaskForm):
  name= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"Name"})
  submit=SubmitField("Edit Author")