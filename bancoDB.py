import sqlite3 as sqlite

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

criar_tabelaClientes()

def criar_tabelaCarros():
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carros(
    id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    ano TEXT NOT NULL,
    quilometragem TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
    
criar_tabelaCarros()

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
    
criar_tabelaVendas()

def inserirClientes(nome, contato, email):
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clientes (nome, contato, email) VALUES (?, ?, ?)
    """, (nome, contato, email))
    conn.commit()
    conn.close()

def inserirCarros(modelo, marca, ano, quilometragem):
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO carros (modelo, marca, ano, quilometragem) VALUES (?, ?, ?, ?)
    """, (modelo, marca, ano, quilometragem))
    conn.commit()
    conn.close()

def listarCarros():
    conn = sqlite.connect('bancoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carros')
    bancoDB = cursor.fetchall()
    carros= []

    for carro in bancoDB:
        carros.append(carro)

    conn.close()
    return carros

