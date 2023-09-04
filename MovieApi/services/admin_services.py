from flask import jsonify, request
from ..model.movie import Movie
from config import db
import json

def add_movie_service(data):

    name = data['name']
    director = data['director']
    genre = json.dumps(['genre']) 
    imdb_score = data['imdb_score']
    popularity = data['popularity']

    new_movie = Movie(name=name, director=director, genre=genre, imdb_score=imdb_score, popularity=popularity)
    db.session.add(new_movie)
    db.session.commit()

    return jsonify({'message': 'Movie added successfully'}), 201



def edit_movie_service(movie_id, data):

    movie = Movie.query.get(movie_id)
    if movie:

        if 'name' in data:
            movie.name = data['name']
        if 'director' in data:
            movie.director = data['director']
        if 'genre' in data:
            movie.genre = json.dumps(data['genre'])
        if 'imdb_score' in data:
            movie.imdb_score = data['imdb_score']
        if 'popularity' in data:
            movie.popularity = data['popularity']

        db.session.commit()
        return jsonify({'message': 'Movie updated successfully'})

    return jsonify({'error': 'Movie not found'}), 404



def delete_movie_service(movie_id):

    movie = Movie.query.get(movie_id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'message': 'Movie deleted successfully'})
    return jsonify({'error': 'Movie not found'}), 404

