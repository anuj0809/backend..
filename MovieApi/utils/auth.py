from ..model.admin import Admin
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity
from functools import wraps
from config import app

jwt = JWTManager(app)

# Check if a user is an admin
def is_admin(username):
    admin_user = Admin.query.filter_by(username=username).first()
    return True if admin_user else False

# Custom decorator to check if a user is an admin
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        if not is_admin(current_user):
            return jsonify({'message': 'Admin privileges required'}), 403
        return fn(*args, **kwargs)
    return wrapper