from flask import jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from ..model.movie import Movie
from ..model.admin import Admin
from ..services.admin_services import add_movie_service, edit_movie_service, delete_movie_service
from ..utils.auth import admin_required
from config import app

@app.route('/login', methods=['POST'])
def login(): 
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    admin_user = Admin.query.filter_by(username=username).first()

    if admin_user and admin_user.password == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/api/movies', methods=['POST'])
@jwt_required()
@admin_required
def add_movie():
    data = request.get_json()
    return add_movie_service(data)

@app.route('/api/movies/<int:movie_id>', methods=['PUT'])
@jwt_required()
@admin_required
def edit_movie(movie_id):
    data = request.get_json()
    return edit_movie_service(movie_id, data)

@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_movie(movie_id):
    return delete_movie_service(movie_id)
