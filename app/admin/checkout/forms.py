from wtforms import SearchField
from flask_wtf import FlaskForm

class CheckoutSearchForm(FlaskForm):
  search=SearchField(render_kw={"placeholder": "Search by user name"})