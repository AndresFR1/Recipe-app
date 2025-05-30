from flask import Blueprint, request, jsonify
from extensions import db, bcrypt
from models import User

register_bp = Blueprint('register_bp', __name__)

@register_bp.route("/api/register", methods=["POST", "OPTIONS"])
def register():
    if request.method == "OPTIONS":
        return '', 200

    data = request.get_json()
    username = data["username"]
    password = data["password"]

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "El usuario ya existe"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuario registrado con éxito"})