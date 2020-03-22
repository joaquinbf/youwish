from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
import op
import json

""" base de datos simulada """
db = None

with open("db.json", "r") as db_file:
    db = json.load(db_file)

""" Se crea un servidor """
app = Flask(__name__)


""" ruta index """
@app.route('/')
def index():
    productos = db["productos"]
    categorias = op.categorias(db)
    marcas = op.marcas(db)
    descuentos = op.descuentos(db)
    return render_template('index.html',
                           productos=productos,
                           categorias=categorias,
                           marcas=marcas,
                           descuentos=descuentos)


""" ruta condicion """
@app.route('/condition/')
def condicion_del_producto():
    c = request.args.get('condicion')
    productos = op.filtrar_por_condicion(db, c)
    categorias = op.categorias(db)
    marcas = op.marcas(db)
    descuentos = op.descuentos(db)
    return render_template('index.html',
                           productos=productos,
                           categorias=categorias,
                           marcas=marcas,
                           descuentos=descuentos)


# Se inicia el servidor en el puerto 4000 del localhost
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=4000)
