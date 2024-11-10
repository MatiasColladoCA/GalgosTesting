from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=root_dir)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la tabla usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

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

    # Guardar datos en la base de datos
    nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, email=email)
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    return send_from_directory(root_dir, 'success.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
