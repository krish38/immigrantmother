from exts import db

class Recipe(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())