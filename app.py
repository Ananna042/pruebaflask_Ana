from flask import Flask, url_for

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

@app.route('/tirar-dado/int:caras>')
def dado(caras):
    from random import randint
    n = randint(1,caras)
    return f"<p>Tire un dado de (caras) caras, salio (n) </p>"



@app.route('/')
def main():
    url_hola = url_for("hello")
    url_dado = url_for("dado", caras=6)
    url_logo = url_for("static", filename="img/logostar.png")

    return f"""
    <a rhef="{url_hola}">Hola</a>
    <br>
    <a href="{url_for("bye")}">Chau</a>
    <br>
    <a href="{url_logo}">Logo</a>
    <br>
    <a href="{url_dado}">Tirar_dado</a>
    """
