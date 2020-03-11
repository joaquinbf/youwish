from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
import op
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
if __name__ == "__main__":
    app.run(debug=True, port=4000)

