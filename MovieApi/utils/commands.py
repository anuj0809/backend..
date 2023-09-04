# Create the database tables if they don't exist
from ..model.movie import Movie
from ..model.admin import Admin
from config import app, db
import json

@app.cli.command('create_db')
def create_db():
    db.create_all()

@app.cli.command('populate_db')
def populate_db():
    # Read the JSON dataset
    # Insert data into the movies table 
    with open('data/imdb.json', 'r') as json_file:
        movies_data = json.load(json_file)

    # Insert data into the movies table
    for movie in movies_data:
        new_movie = Movie(
            popularity=movie['99popularity'],
            director=movie['director'],
            genre=json.dumps(movie['genre']),
            imdb_score=movie['imdb_score'],
            name=movie['name']
        )
        db.session.add(new_movie)

    with open('data/admin.json', 'r') as json_file:
        admin_data = json.load(json_file)

    for admin in admin_data:
        new_admin = Admin(
            username = admin['username'],
            password = admin['password']
        )
        db.session.add(new_admin)

    db.session.commit()

