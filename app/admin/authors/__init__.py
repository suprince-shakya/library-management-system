from flask import Blueprint

bp=Blueprint('author',__name__)

from app.admin.authors import routes