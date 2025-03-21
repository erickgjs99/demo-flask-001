"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo con Flask</h1>"

@app.route('/suma')
def suma():
    resultado = 5 + 5
    return "<h3>10 + 10 = %d</h3>" % (resultado)


@app.route('/listado')
def listado():
    return "<h3>Mejores Amigos</h3><ol><li>David Salazar</li><li>David Pillco</li><li>Kevin Proaño</li><li>Jean Paul Reyes</li><li>Alan Flores</li><li>Ricardo Salvatierra</li></ol> " 

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
