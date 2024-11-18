from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv('.env')
class Config:
  APP_HOST = os.environ.get('APP_HOST')
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = False