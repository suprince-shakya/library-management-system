from wtforms import StringField,SubmitField,SearchField,FloatField,FileField,IntegerField,SelectField,TextAreaField
from wtforms.validators import InputRequired,Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import FlaskForm

class BookSearchForm(FlaskForm):
  search=SearchField(render_kw={"placeholder": "Search Book"})

class AddBookForm(FlaskForm):
  name= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"Book Name"})
  category_id= SelectField('Select Category',choices=[],coerce=int,validate_choice=False)
  author_id= SelectField('Select Author',choices=[],coerce=int,validate_choice=False)
  isbn= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"ISBN Number"})
  price= FloatField(validators=[InputRequired()],render_kw={"placeholder":"Price"})
  quantity= IntegerField(validators=[InputRequired()],render_kw={"placeholder":"Quantity"})
  picture= FileField(validators=[FileRequired(),FileAllowed(['jpeg','jpg', 'png'], 'Images only!')])
  description=TextAreaField(validators=[Length(min=2)],render_kw={"placeholder":"Description"})
  submit=SubmitField("Add Book")

class EditBookForm(FlaskForm):
  name= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"Book Name"})
  category_id= SelectField('Select Category',choices=[],coerce=int,validate_choice=False)
  author_id= SelectField('Select Author',choices=[],coerce=int,validate_choice=False)
  isbn= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"ISBN Number"})
  price= FloatField(validators=[InputRequired()],render_kw={"placeholder":"Price"})
  quantity= IntegerField(validators=[InputRequired()],render_kw={"placeholder":"Quantity"})
  description=TextAreaField(validators=[Length(min=2)],render_kw={"placeholder":"Description"})
  picture= FileField(validators=[FileAllowed(['jpeg','jpg', 'png'], 'Images only!')])
  submit=SubmitField("Edit Book")