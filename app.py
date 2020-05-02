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
    """ se pide la condicion enviada por parametro junto el request"""
    c = request.args.get('condicion')

    """ se filtra segun la condicion """
    productos = op.filtrar_por_condicion(db, c)

    """ se obtienen el resto de los datos necesarios para renderizar """
    categorias = op.categorias(db)
    marcas = op.marcas(db)
    descuentos = op.descuentos(db)
    return render_template('index.html',
                           productos=productos,
                           categorias=categorias,
                           marcas=marcas,
                           descuentos=descuentos)

""" ruta ordenar """
@app.route('/ordenar/')
def ordenar_productos():
    """ se pide el tipo de orden que se solicita en el request """
    o = request.args.get('orden')

    """ se ordenan los productos segun el tipo orden solicitado """
    productos = op.ordenar_productos(db, o)

    """ se obtienen el resto de los datos necesarios para renderizar """
    categorias = op.categorias(db)
    marcas = op.marcas(db)
    descuentos = op.descuentos(db)
    return render_template('index.html',
                           productos=productos,
                           categorias=categorias,
                           marcas=marcas,
                           descuentos=descuentos)

""" ruta categorias """
@app.route('/categorias/')
def filtrar_por_categoria():
    """ se pide la categoria solicitado en el request """
    c = request.args.get('categoria')

    """ se filtran los productos segun la categoria """
    productos = op.filtrar_por_categoria(db, c)

    """ se obtienen el resto de los datos necesarios para renderizar """
    categorias = op.categorias(db)
    marcas = op.marcas(db)
    descuentos = op.descuentos(db)
    return render_template('index.html',
                           productos=productos,
                           categorias=categorias,
                           marcas=marcas,
                           descuentos=descuentos)

""" ruta descuentos """
@app.route('/descuentos/')
def filtrar_por_descuento():
    """ se pide el valor del descuento solicitado en el request """
    d = request.args.get('descuento')

    """ se filtran los productos segun el descuento """
    productos = op.filtrar_por_descuento(db, d)

    """ se obtienen el resto de los datos necesarios para renderizar """
    categorias = op.categorias(db)
    marcas = op.marcas(db)
    descuentos = op.descuentos(db)
    return render_template('index.html',
                           productos=productos,
                           categorias=categorias,
                           marcas=marcas,
                           descuentos=descuentos)

""" ruta marcas """
@app.route('/marcas/')
def filtrar_por_marca():
    """ se pide a la marca solicitada en el request """
    m = request.args.get('marca')

    """ se filtran los productos segun la marca """
    productos = op.filtrar_por_marca(db, m)

    """ se obtienen el resto de los datos necesarios para renderizar """
    categorias = op.categorias(db)
    marcas = op.marcas(db)
    descuentos = op.descuentos(db)
    return render_template('index.html',
                           productos=productos,
                           categorias=categorias,
                           marcas=marcas,
                           descuentos=descuentos)

""" ruta calificaciones """
@app.route('/calificaciones/')
def filtrar_por_calificacion():
    """ se pide a la marca solicitada en el request """
    c = request.args.get('calificacion')

    """ se filtran los productos segun la marca """
    productos = op.filtrar_por_calificacion(db, c)

    """ se obtienen el resto de los datos necesarios para renderizar """
    categorias = op.categorias(db)
    marcas = op.marcas(db)
    descuentos = op.descuentos(db)
    return render_template('index.html',
                           productos=productos,
                           categorias=categorias,
                           marcas=marcas,
                           descuentos=descuentos)

""" ruta rango de precios """
@app.route('/rango_precio/')
def filtrar_segun_rengo_precios():
    """ se pide el minimo y maximo valor del rango en el request """
    m = request.args.get('min')
    M = request.args.get('max')

    """ se filtran los productos segun el maximo y minimo valor """
    productos = op.filtrar_por_rango_precios(db, m, M)

    """ se obtienen el resto de los datos necesarios para renderizar """
    categorias = op.categorias(db)
    marcas = op.marcas(db)
    descuentos = op.descuentos(db)
    return render_template('index.html',
                           productos=productos,
                           categorias=categorias,
                           marcas=marcas,
                           descuentos=descuentos)



""" ruta busqueda """
@app.route('/busqueda/')
def bucar_productos():
    """ se piden las palabras enviadas por parametro junto al request """
    p = request.args.get('buscar')

    """ se filtra por nombre y descripcion del producto """
    productos = op.buscar_productos(db, p)

    """ se obtienen el resto de los datos necesarios para renderizar """
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
