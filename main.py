from flask import Flask, render_template, request

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
    carros = bancoDB.listarCarros()
    return render_template("realizarVendas.html", carros=carros)

@app.route("/carrosVendidos")
def carrosVendidos():
    carros = bancoDB.listarCarrosIndisponiveis()
    return render_template("carrosVendidos.html", carros=carros)

@app.route("/salvarCarros", methods=['POST'])
def salvarCarros():
    modelo = request.form.get("modelo")
    marca = request.form.get("marca")
    preco = request.form.get("preco")
    ano = str(request.form.get("fabricacao"))
    quilometragem = str(request.form.get("quilometragem"))
    bancoDB.inserirCarros(modelo, marca, preco, ano, quilometragem)
    return render_template("cadastrarCarros.html", mensagem="Carro cadastrado com sucesso!")

@app.route("/salvarClientes", methods=['POST'])
def salvarClientes():
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    email = request.form.get("email")
    bancoDB.inserirClientes(nome, telefone, email)
    mensagem="Cliente cadastrado com sucesso!"
    return render_template("cadastrarClientes.html", mensagem=mensagem)



@app.route("/salvarVenda", methods=['POST'])
def salvarVenda():
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    email = request.form.get("email")
    id_carro = request.form.get("id_carro")


    id_cliente = bancoDB.buscarCliente(nome, telefone, email)

    print(id_cliente)
    print(id_carro)

    if not id_cliente:
        return render_template("realizarVendas.html", mensagem="Erro: Cliente não encontrado.", carros=bancoDB.listarCarros())


    carro = bancoDB.buscarCarroDisponivel(id_carro)
    if not carro:
        return render_template("realizarVendas.html", mensagem="Erro: Carro não disponível ou inexistente.", carros=bancoDB.listarCarros())


    bancoDB.inserirVenda(id_carro, id_cliente)

    bancoDB.atualizarDisponibilidadeCarro(id_carro, 0)

    return render_template("realizarVendas.html", mensagem="Venda realizada com sucesso!", carros=bancoDB.listarCarros())



app.run(debug=True)
