from flask import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastrarCarros")
def cadastrarCarros():
    return render_template("cadastrarCarros.html")

@app.route("/cadastrarClientes")
def cadastrarClientes():
    return render_template("cadastrarClientes.html")

@app.route("/realizarVendas")
def realizarVendas():
    return render_template("realizarVendas.html")


app.run(debug=True)