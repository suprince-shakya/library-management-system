from flask_wtf import FlaskForm
from wtforms import PasswordField,SubmitField
from wtforms.validators import InputRequired,Length

class ChangePasswordForm(FlaskForm):
  current_pass= PasswordField(validators=[InputRequired(), Length(min=3,max=50)],render_kw={"placeholder":"Current Password"})
  new_pass= PasswordField(validators=[InputRequired(), Length(min=3,max=50)],render_kw={"placeholder":"New Password"})
  confirm_pass= PasswordField(validators=[InputRequired(), Length(min=3,max=50)],render_kw={"placeholder":"Confirm Password"})
  submit=SubmitField("Submit")