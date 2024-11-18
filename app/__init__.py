from flask import Flask,render_template
from config import Config
from app.extensions import db,bcrypt,login_manager,seeder
from flask_migrate import Migrate
from app.models.user import User
from app.models.category import Category
from app.models.author import Author
from app.models.book import Book
from app.models.book_request import BookRequest
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

def create_app(config_class=Config):
  # Initialize flask app
  app=Flask(__name__)
  app.config.from_object(config_class)
 
  app.secret_key=app.config.get('SECRET_KEY')

  # Initialize extensions
  bcrypt.init_app(app)
  login_manager.init_app(app)
  login_manager.login_view='login'

  # Create database if not exists
  engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
  if not database_exists(engine.url):
    create_database(engine.url)

  # Initialize Database
  db.init_app(app)
  migrate=Migrate(app,db)

  # Initialize Seeders
  seeder.init_app(app,db)

  # Register blueprints here
  from app.main import bp as main_bp
  app.register_blueprint(main_bp)

  from app.admin import bp as admin_bp
  app.register_blueprint(admin_bp, url_prefix="/admin")

  @app.errorhandler(404)
  def page_not_found(e):
    return render_template('404.html')

  return app