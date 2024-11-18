from flask_seeder import Seeder,Faker
from app.models.user import User,RolesEnum
from app.extensions import bcrypt

class AdminUserSeeder(Seeder):
  def run(self):
    user=User(firstname="Admin",lastname="admin",email="john.doe@gmail.com",password=bcrypt.generate_password_hash("admin123"),role=RolesEnum.Admin.name)
    self.db.session.add(user)