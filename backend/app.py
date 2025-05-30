from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from extensions import db, bcrypt, jwt


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@localhost:3306/mysql93'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '444111'

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

API_URL = "https://www.themealdb.com/api/json/v1/1"

@app.route("/api/search")
def search_recipes():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Falta el parámetro de búsqueda"}), 400

    response = requests.get(f"{API_URL}/search.php", params={"s": query})
    if response.status_code != 200:
        return jsonify({"error": "Error al consultar la API externa"}), 500

    data = response.json()
    return jsonify(data)

@app.route("/api/recipe/<id>")
def get_recipe(id):
    response = requests.get(f"{API_URL}/lookup.php", params={"i": id})
    if response.status_code != 200:
        return jsonify({"error": "Error al consultar la API externa"}), 500

    data = response.json()
    return jsonify(data)

import models
from RegisterRoute import register_bp
from LoginRoute import login_bp

app.register_blueprint(register_bp)
app.register_blueprint(login_bp)

if __name__ == "__main__":
    app.run(debug=True)
