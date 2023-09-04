from flask import jsonify
from ..model.movie import Movie
import json

def get_movies_service():
    #logic here 
    movies = Movie.query.all()
    movie_list = []
    for movie in movies:
        movie_dict = {
            'id': movie.id,
            'popularity': movie.popularity,
            'director': movie.director,
            'genre': json.loads(movie.genre),
            'imdb_score': movie.imdb_score,
            'name': movie.name
        }
        movie_list.append(movie_dict)
    return jsonify({'movies': movie_list})

def search_movies_service(genre, name, director, query_params):
    #logic here 
    movies_query = Movie.query
    if genre:
        movies_query = movies_query.filter(Movie.genre.contains(genre))

    if name:
        movies_query = movies_query.filter(Movie.name.ilike(f'%{name}%'))

    if director:
        movies_query = movies_query.filter(Movie.director.ilike(f'%{director}%'))


    movies_query = movies_query.filter_by(**query_params).all()

    movie_list = []
    for movie in movies_query:
        movie_dict = {
            'id': movie.id,
            'popularity': movie.popularity,
            'director': movie.director,
            'genre': json.loads(movie.genre),
            'imdb_score': movie.imdb_score,
            'name': movie.name
        }
        movie_list.append(movie_dict)

    return jsonify({'movies': movie_list})

