from flask import Flask
from flask import render_template
import json

# Se crea un servidor
app = Flask(__name__)


# ruta index
@app.route('/')
def index():
    return render_template('index.html')

# ruta productos
@app.route('/')
def productos():
    productos = json.loads('db.json')
    return productos

# Se inicia el servidor en el puerto 4000 del localhost
app.run(debug=True, port=4000)

