from flask_seeder import Seeder
from app.models.author import Author

authors=['Elle Marr','Emily Henry','Alastair Reynolds','Stephen Graham Jones','F. Scott Fitzgerald','Spencer Johnson','Jane Austen','Héctor García','Paulo Coelho','Robert Kiyosaki']

class AuthorSeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 10
    
  def run(self):
    for author in authors:
      self.db.session.add(Author(name=author))
 