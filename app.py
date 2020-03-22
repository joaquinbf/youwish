from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
import op
import json

db = None

with open("db.json", "r") as db_file:
    db = json.load(db_file)

# Se crea un servidor
app = Flask(__name__)


# ruta index
@app.route('/')
def index():
    productos = db["productos"]
    return render_template('index.html', productos=productos)



# Se inicia el servidor en el puerto 4000 del localhost
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=4000)
