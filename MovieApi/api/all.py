from flask import jsonify, request
from ..model.movie import Movie
from ..services.all_services import get_movies_service, search_movies_service
from config import app

@app.route('/api/movies', methods=['GET'])
def get_movies():
    return get_movies_service()

@app.route('/api/movies', methods=['GET'])
def search_movies():
    query_params = request.args.to_dict()

    genre = query_params.pop('genre', None)  
    name = query_params.pop('name', None)    
    director = query_params.pop('director', None)    

    return search_movies_service(genre, name, director, query_params)
