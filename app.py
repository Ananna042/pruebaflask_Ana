from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/chau')
def chau():
    return 'Adios!'

@app.route('/saludar/por-nombre/<string:nombre>')
def sxn(nombre):
    return f"<p>Hola {nombre}</p>"

