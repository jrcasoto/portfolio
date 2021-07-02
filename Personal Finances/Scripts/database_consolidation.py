import sqlite3
import os


def check_db():
    # Remover duplicatas para primeiro processamento em máquina local
    os.remove("finance.db") if os.path.exists("finance.db") else None
    return True


def create_connection():
    # Estabelecer conexão e criar cursor para criar tabelas
    db = sqlite3.connect("finance.db")
    return db


def create_tables(c):
    # Criar tabela Balanço patrimonial
    c.execute("CREATE TABLE balanco_patrimonial_pessoal( \
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
        data_ref DATE NOT NULL, \
        ativo_passivo TEXT NOT NULL, \
        fixo_variavel TEXT NOT NULL, \
        circulante TEXT NOT NULL)")
    # Criar tabela Rendimentos
    c.execute("CREATE TABLE rendimentos( \
        cod_ativo TEXT PRIMARY KEY NOT NULL, \
        rendimento_cota REAL NOT NULL, \
        data_ref DATE NOT NULL)")
    # Criar tabela Lançamentos
    c.execute("CREATE TABLE lancamentos( \
        cod_ativo TEXT PRIMARY KEY NOT NULL, \
        data_ref DATE NOT NULL, \
        qtde INTEGER NOT NULL, \
        valor_unit REAL NOT NULL, \
        tipo TEXT NOT NULL)")
    # Criar tabela Custódia (trabalhar nos dados antes de criar colunas calculadas)
    # c.execute("CREATE TABLE custodia()")
    return True


def close_connection(db, c):
    # Fechar cursor e conexão com banco
    c.close()
    db.close()
    return True


def main():
    check_db()

    db = create_connection()
    c = db.cursor()
    create_tables(c)

    close_connection(db, c)


main()