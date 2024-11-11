from flask import Flask, request, jsonify, render_template, send_from_directory
from pymongo import MongoClient
import os

app = Flask(__name__, template_folder='.')

# Configuración de la URI de MongoDB
MONGODB_URI = "mongodb://atlas-sql-67252c88077cc50840802c62-fugqw.a.query.mongodb.net/sample_mflix?ssl=true&authSource=admin"
client = MongoClient(MONGODB_URI)

# Selección de la base de datos y colección
db = client['sample_mflix']  # Cambia 'sample_mflix' al nombre de tu base de datos si es diferente
usuarios_collection = db['usuarios']  # Puedes cambiar 'usuarios' al nombre que desees para la colección

# Ruta principal para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar los datos del formulario
@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    email = request.form.get('email')

    # Guardar datos en MongoDB
    nuevo_usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email
    }
    usuarios_collection.insert_one(nuevo_usuario)
    
    return send_from_directory('.', 'success.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
