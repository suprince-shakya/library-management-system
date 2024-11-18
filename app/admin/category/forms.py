from wtforms import StringField,SubmitField,RadioField,SearchField
from wtforms.validators import InputRequired,Length
from flask_wtf import FlaskForm

class CategorySearchForm(FlaskForm):
  search=SearchField(render_kw={"placeholder": "Search Category"})

class AddCategoryForm(FlaskForm):
  title= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"Title"})
  status= RadioField('Status',choices=[(True,'Active'),(False,'Inactive')])
  submit=SubmitField("Add Category")

class EditCategoryForm(FlaskForm):
  title= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"Title"})
  status= RadioField('Status',choices=[(True,'Active'),(False,'Inactive')])
  submit=SubmitField("Edit Category")