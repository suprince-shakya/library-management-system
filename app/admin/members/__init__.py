from flask import Blueprint

bp=Blueprint('member',__name__)

from app.admin.members import routes