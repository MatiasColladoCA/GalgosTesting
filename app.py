from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configura la conexión a MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:agzJnxNrRGmcdaexwwAYqpBgKvYuKKxp@autorack.proxy.rlwy.net:27837/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de ejemplo para la tabla "Usuario"
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Inicializar la base de datos
with app.app_context():
    db.create_all()

# Ruta de ejemplo
@app.route('/')
def index():
    return "Conexión con MySQL en Railway exitosa!"

if __name__ == '__main__':
    app.run(debug=True)
