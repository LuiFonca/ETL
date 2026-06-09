import pandas as pd
from sqlalchemy import create_engine


# CONFIGURAÇÃO MYSQL

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = ""
DATABASE = "olist_etl"


def conectar_mysql():

    return create_engine(
        "mysql+pymysql://root@localhost/olist_etl"
    )


def listar_tabelas():

    engine = conectar_mysql()

    query = """
    SHOW TABLES
    """

    tabelas = pd.read_sql(query, engine)

    return tabelas.iloc[:, 0].tolist()


def carregar_tabela_mysql(nome_tabela):

    engine = conectar_mysql()

    query = f"""
    SELECT *
    FROM {nome_tabela}
    """

    return pd.read_sql(query, engine)


def carregar_tabela_paginada(
    nome_tabela,
    limite=50,
    offset=0
):

    engine = conectar_mysql()

    query = f"""
    SELECT *
    FROM {nome_tabela}
    LIMIT {limite}
    OFFSET {offset}
    """

    return pd.read_sql(query, engine)


def contar_registros(nome_tabela):

    engine = conectar_mysql()

    query = f"""
    SELECT COUNT(*) AS total
    FROM {nome_tabela}
    """

    resultado = pd.read_sql(query, engine)

    return int(resultado["total"][0])


def pesquisar_tabela(
    nome_tabela,
    coluna,
    termo
):

    engine = conectar_mysql()

    query = f"""
    SELECT *
    FROM {nome_tabela}
    WHERE {coluna}
    LIKE '%{termo}%'
    LIMIT 100
    """

    return pd.read_sql(query, engine)