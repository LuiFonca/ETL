from sqlalchemy import create_engine
import pandas as pd

# CONEXÃO MYSQL

engine = create_engine(
    "mysql+pymysql://root@localhost/olist_etl"
)


# LISTAR TABELAS

def listar_tabelas():

    query = "SHOW TABLES"

    tabelas = pd.read_sql(
        query,
        engine
    )

    return tabelas.iloc[:, 0].tolist()


# CARREGAR TABELA

def carregar_tabela_mysql(nome_tabela):

    query = f"""
    SELECT *
    FROM {nome_tabela}
    """

    return pd.read_sql(
        query,
        engine
    )