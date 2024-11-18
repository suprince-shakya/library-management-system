from flask_seeder import Seeder
from app.models.category import Category

categories=['Romance','Novel','Self-help','Friction','Fantasy','Horror','Action & Adventure','Science Fiction','Detective & Mystery','Thriller & Suspense']

class CategorySeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 10

  def run(self):
    for category in categories:
      self.db.session.add(Category(title=category,status=True))
 