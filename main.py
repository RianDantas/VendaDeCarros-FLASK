from flask import *

app = Flask(__name__)

import bancoDB


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


@app.route("/salvarCarros", methods=['POST'])
def salvarCarros():
    modelo = request.form.get("modelo")
    marca = request.form.get("marca")
    ano = request.form.get("fabricacao")
    quilometragem = str(request.form.get("quilometragem"))

    bancoDB.inserirCarros(modelo, marca, ano, quilometragem)

    mensagem = "Carro cadastrado com sucesso!"
    return render_template("cadastrarCarros.html", modelo = mensagem)

@app.route("/salvarClientes", methods=['POST'])
def salvarClientes():
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    email = request.form.get("email")

    mensagem = "nome: " + nome + "," + "telefone: " + telefone + "," + " ano de fabricação: " + email 
    return render_template("cadastrarClientes.html", modelo = mensagem)


@app.route("/carrosDisponiveis")
def carrosDisponiveis():
    carros = bancoDB.listarCarros()

    return render_template("carrosDisponiveis.html", carros = carros)


app.run(debug=True)