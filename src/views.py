from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from .utils import form_recognizer

d = form_recognizer.datos

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("index.html")
    

@views.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@views.route('/register', methods=['GET'])
def register():
    return render_template("register.html")


@views.route('/createA', methods=['GET'])
def createA():
    return render_template("createA.html")


@views.route('/createP', methods=['GET'])
def createP():
    return render_template("createP.html")


@views.route('/createP2', methods=['GET'])
def createP2():
    return render_template("createP2.html", dic=d, nombre="FirstName", apellido="LastName", edad=str(2022-d["DateOfBirth"].year))


@views.route('/createPF', methods=['GET'])
def createPF():
    return render_template("createPF.html")


@views.route('/seccionar', methods=['GET'])
def seccionar():
    return render_template("seccionar.html")


@views.route('/vProfesor', methods=['GET'])
def vProfesor():
    return render_template("vProfesor.html")


@views.route('/Notificaciones', methods=['GET'])
def Notificaciones():
    return render_template("Notificaciones.html")


@views.route('/sscurso', methods=['GET'])
def sscurso():
    return render_template("sscurso.html")


@views.route('/createPF2', methods=['GET'])
def createPF2():
    return render_template("createPF2.html")


@views.route('/revision', methods=['GET'])
def revision():
    return render_template("revision.html")


@views.route('/gView', methods=['GET'])
def gView():
    return render_template("gView.html")


@views.route('/felicidades', methods=['GET'])
def felicidades():
    return render_template("felicidades.html")


@views.route('/sHorario', methods=['GET'])
def sHorario():
    return render_template("sHorario.html")


@views.route('/sHora', methods=['GET'])
def sHora():
    return render_template("sHora.html")


@views.route('/sAsesoria', methods=['GET'])
def sAsesoria():
    return render_template("sAsesoria.html")


@views.route('/vPadre', methods=['GET'])
def vPadre():
    return render_template("vPadre.html")


@views.route('/test-form', methods=['GET'])
def test_form():
    return render_template("test-form.html", dic=d, nombre="FirstName", apellido="LastName", edad=str(2022-d["DateOfBirth"].year))


@views.route('/test', methods=['GET'])
def test():
    return render_template("test.html")


@views.route('/aprobado', methods=['GET'])
def aprobado():
    return render_template("aprobado.html")


@views.route('/curso', methods=['GET'])
def curso():
    return render_template("curso.html")


@views.route('/curso2', methods=['GET'])
def curso2():
    return render_template("curso2.html")


@views.route('/pruebaC', methods=['GET'])
def pruebaC():
    return render_template("pruebaC.html")


@views.route('/dAyuda', methods=['GET'])
def dAyuda():
    return render_template("dAyuda.html")


@views.route('/nAyuda', methods=['GET'])
def nAyuda():
    return render_template("nAyuda.html")


@views.route('/perfil', methods=['GET'])
def perfil():
    return render_template("perfil.html")
