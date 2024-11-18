from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField,SearchField
from wtforms.validators import InputRequired,Length,ValidationError
from app.models.user import User

class BookSearchForm(FlaskForm):
  search=SearchField(render_kw={"placeholder": "Search Book"})

class LoginForm(FlaskForm):
  email= EmailField(validators=[InputRequired(), Length(min=4,max=50)],render_kw={"placeholder":"Email"})
  password= PasswordField(validators=[InputRequired(), Length(min=4,max=50)],render_kw={"placeholder":"Password"})
  submit=SubmitField("Login")

class ChangePasswordForm(FlaskForm):
  current_pass= PasswordField(validators=[InputRequired(), Length(min=3,max=50)],render_kw={"placeholder":"Current Password"})
  new_pass= PasswordField(validators=[InputRequired(), Length(min=3,max=50)],render_kw={"placeholder":"New Password"})
  confirm_pass= PasswordField(validators=[InputRequired(), Length(min=3,max=50)],render_kw={"placeholder":"Confirm Password"})
  submit=SubmitField("Submit")

class EditProfileForm(FlaskForm):
  firstname= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"Firstname"})
  lastname= StringField(validators=[InputRequired(), Length(min=3,max=20)],render_kw={"placeholder":"Lastname"})
  email= EmailField(render_kw={"placeholder":"Email"})
  submit=SubmitField("Edit Profile")

class RegisterForm(FlaskForm):
  firstname= StringField(validators=[InputRequired(), Length(min=2,max=50)],render_kw={"placeholder":"Firstname"})
  lastname= StringField(validators=[InputRequired(), Length(min=2,max=50)],render_kw={"placeholder":"Lastname"})
  email= EmailField(validators=[InputRequired(), Length(min=4,max=50)],render_kw={"placeholder":"Email"})
  password= PasswordField(validators=[InputRequired(), Length(min=4,max=50)],render_kw={"placeholder":"Password"})
  submit=SubmitField("Register")

  def validate_email(self,email):
    existing_user=User.query.filter_by(email=email.data).first()
    if existing_user:
      raise ValidationError("Email already taken. Please choose different one.")