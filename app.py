from flask import Flask, render_template, request, render_template_string
from jinja2 import Markup

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route("/reflejado1/", methods=["GET","POST"])
def reflejado1():
    if request.method == "POST":
        comentario = request.form.get("comentario")
        return comentario
    return render_template("xssreflejado/reflejado1.html")

@app.route("/reflejado2/", methods=["GET","POST"])
def reflejado2():
    if request.method == "POST":
        comentario = request.form.get("comentario")
        return render_template_string(comentario)
    return render_template("xssreflejado/reflejado2.html")

@app.route("/reflejado3/", methods=["GET","POST"])
def reflejado3():
    comentario = ""
    if request.method == "POST":
        comentario = request.form.get("comentario")
    return render_template("xssreflejado/reflejado3.html", comentario=Markup(comentario))

@app.route("/reflejado4/", methods=["GET","POST"])
def reflejado4():
    comentario = ""
    if request.method == "POST":
        comentario = request.form.get("comentario")
    return render_template("xssreflejado/reflejado4.html", comentario=comentario)

@app.route("/reflejado5/", methods=["GET","POST"])
def reflejado5():
    comentario = ""
    if request.method == "POST":
        comentario = request.form.get("comentario")
    return render_template("xssreflejado/reflejado5.html", comentario=comentario)

if __name__ == '__main__':
    app.run()
