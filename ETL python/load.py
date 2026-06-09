from sqlalchemy import create_engine



# CONEXÃO COM O BANCO DE DADOS


engine = create_engine(
    "mysql+pymysql://root@localhost/olist_etl"
)



# FUNÇÃO DE CARGA


def carregar_tabela(df, nome_tabela):

    print(f"Carregando tabela {nome_tabela}...")

    df.to_sql(
        nome_tabela,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"Tabela {nome_tabela} carregada com sucesso!")