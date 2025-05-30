from flask import Blueprint, request, jsonify
from extensions import db, bcrypt
from models import User
from flask_jwt_extended import create_access_token

login_bp = Blueprint('login_bp', __name__)

@login_bp.route("/api/login", methods=["POST", "OPTIONS"])
def login():
    if request.method == "OPTIONS":
        return '', 200

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"message": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token, "message": "Inicio de sesión exitoso"})
