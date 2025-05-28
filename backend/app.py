from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
# Importar las bibliotecas necesarias


app = Flask(__name__)
CORS(app)

API_URL = "https://www.themealdb.com/api/json/v1/1" # URL base de la API externa

@app.route("/api/search")
# Definición de la ruta `/api/search` Le dice a Flask que la función que sigue (`search_recipes`) debe ejecutarse cada vez que una petición HTTP
# (por defecto, GET) llegue a la URL `/api/search` en tu servidor Flask.

def search_recipes(): # Función para buscar recetas - Define la función de Python que manejará las peticiones a la ruta `/api/search`.

    query = request.args.get("q") # Obtener el parámetro de búsqueda

    if not query: # Verificación del parámetro de búsqueda
    
        return jsonify({"error": "Missing query parameter"}), 400 # Retornar error si falta el parámetro
        
        
    response = requests.get(f"{API_URL}/search.php?s={query}") # Hacer la petición a la API de TheMealDB
    
    return jsonify(response.json()) # Retornar la respuesta de la API 
    

@app.route("/api/recipe/<id>") # Definición de la ruta `/api/recipe/<id>` Esta ruta está diseñada para obtener una receta específica por su ID.

def get_recipe(id): #Función para obtener una receta por ID

    response = requests.get(f"{API_URL}/lookup.php?i={id}") # Hacer la petición a la API xterna para obtener una receta por ID

    return jsonify(response.json()) # Retornar la respuesta de la API 

if __name__ == "__main__": # Bloque de ejecución principal
    app.run(debug=True) # Iniciar el servidor Flask
    