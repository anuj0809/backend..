from config import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    popularity = db.Column(db.Float)
    director = db.Column(db.String(255))
    genre = db.Column(db.Text)  # Store JSON data as text
    imdb_score = db.Column(db.Float)
    name = db.Column(db.String(255))