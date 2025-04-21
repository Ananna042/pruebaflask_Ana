from flask import Flask, url_for
from flask import render_template
import sqlite3
app = Flask(__name__)

def dict_factory(cursor,row):
    """Arama un dicc con los valores e la fila"""
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

db = None
def abrirConexion():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = dict_factory

def cerrarConexion():
    global db 
    db.close()
    db = None

@app.route("/test-db")
def testDB():
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT(*) AS cant FROM usuarios; ")
    res = cursor.fetchone()
    registros = res["cant"]
    cerrarConexion()
    return f"Hay {registros} registros en la tabla de usuario"

@app.route("/crear-usuario")#EJ PARA HACER ACT PERO CON 2 ARG
def testCrear():
    nombre = "leandro"
    email = "leandro@etec.uba.ar"
    abrirConexion()
    cursor = db.cursor()
    consulta = "INSERT INTO usuarios(usuario, email) VALUES (?, ?)"
    cursor.execute(consulta, (nombre, email))
    db.commit()
    cerrarConexon()
    return f"Registro agregado ({nombre                                                                                                                                                                                                                                                                                                                                                                                                                                      })"




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



@app.route("/mostrar-datos/<int:id>")
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id,usuario, email FROM usuarios WHERE id = ?",(id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email = None
    if res != None:
        usuario = res['usuario']
        email = res ['email']
    return render_template("datos.html", id=id, usuario=usuario, email=email)