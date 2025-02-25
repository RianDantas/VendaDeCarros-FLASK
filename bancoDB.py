import sqlite3 as sqlite

def criar_banco():
    criar_tabelaClientes()
    criar_tabelaCarros()
    criar_tabelaVendas()

def criar_tabelaClientes():
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    contato TEXT NOT NULL,
    email TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def criar_tabelaCarros():
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carros(
    id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    preco TEXT NOT NULL,
    ano TEXT NOT NULL,
    quilometragem TEXT NOT NULL,
    disponivel BOOLEAN NOT NULL DEFAULT 1
    )
    ''')
    conn.commit()
    conn.close()

def criar_tabelaVendas():
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas(
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    id_carro INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL,
    FOREIGN KEY (id_carro) REFERENCES carros(id_carro),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
    )
    """)
    conn.commit()
    conn.close()

def inserirClientes(nome, contato, email):
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, contato, email) VALUES (?, ?, ?)", (nome, contato, email))
    conn.commit()
    conn.close()

def inserirCarros(modelo, marca, preco, ano, quilometragem):
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO carros (modelo, marca, preco, ano, quilometragem, disponivel) VALUES (?, ?, ?, ?, ?, 1)", (modelo, marca, preco, ano, quilometragem))
    conn.commit()
    conn.close()

def inserirVenda(id_carro, id_cliente):
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vendas (id_carro, id_cliente) VALUES (?, ?)", (id_carro, id_cliente))
    cursor.execute("UPDATE carros SET disponivel = 0 WHERE id_carro = ?", (id_carro,))
    conn.commit()
    conn.close()

def listarCarros():
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carros WHERE disponivel = 1")
    carros = cursor.fetchall()
    conn.close()
    return carros

def listarCarrosIndisponiveis():
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carros WHERE disponivel = 0")
    carros = cursor.fetchall()
    conn.close()
    return carros

def buscarCliente(nome, telefone, email):
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT id_cliente FROM clientes WHERE nome = ? AND contato = ? AND email = ?", (nome, telefone, email))
    cliente = cursor.fetchone()
    conn.close()
    return cliente[0] if cliente else None

def buscarCarroDisponivel(id_carro):
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carros WHERE id_carro = ? AND disponivel = 1", (id_carro,))
    carro = cursor.fetchone()
    conn.close()
    return carro

def atualizarDisponibilidadeCarro(id_carro, disponivel):
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    query = "UPDATE carros SET disponivel = ? WHERE id_carro = ?"
    cursor.execute(query, (disponivel, id_carro))
    conn.commit()

criar_banco()