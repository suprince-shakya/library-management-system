from flask import Blueprint

bp=Blueprint('checkout',__name__)

from app.admin.checkout import routes