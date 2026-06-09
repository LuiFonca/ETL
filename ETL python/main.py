from extract import carregar_dados

from transform import (
    tratar_customers,
    tratar_geolocation,
    tratar_order_items,
    tratar_order_payments,
    tratar_order_reviews,
    tratar_orders,
    tratar_products,
    tratar_sellers
)

from load import carregar_tabela


# RELATÓRIO DE QUALIDADE


def analisar_dataframe(nome, df):
    print("\n" + "=" * 70)
    print(f"TABELA: {nome}")
    print("=" * 70)

    print(f"Linhas: {len(df):,}")
    print(f"Colunas: {len(df.columns)}")
    print(f"Duplicados: {df.duplicated().sum():,}")

    nulos = df.isnull().sum()
    nulos = nulos[nulos > 0]

    if len(nulos) > 0:
        print("\nCOLUNAS COM VALORES NULOS:")

        for coluna, qtd in nulos.items():
            percentual = (qtd / len(df)) * 100

            print(
                f"- {coluna}: "
                f"{qtd:,} registros "
                f"({percentual:.2f}%)"
            )
    else:
        print("\nNenhum valor nulo encontrado.")

    print("\nTipos das colunas:")
    print(df.dtypes)


# EXTRACT

tabelas = carregar_dados()


# RELATÓRIO ANTES


print("\n")
print("#" * 70)
print("RELATÓRIO ANTES DA TRANSFORMAÇÃO")
print("#" * 70)

for nome, df in tabelas.items():
    analisar_dataframe(nome, df)


# TRANSFORM


tabelas["Customers"] = tratar_customers(tabelas["Customers"])
tabelas["Geolocation"] = tratar_geolocation(tabelas["Geolocation"])
tabelas["Order Items"] = tratar_order_items(tabelas["Order Items"])
tabelas["Order Payments"] = tratar_order_payments(tabelas["Order Payments"])
tabelas["Order Reviews"] = tratar_order_reviews(tabelas["Order Reviews"])
tabelas["Orders"] = tratar_orders(tabelas["Orders"])
tabelas["Products"] = tratar_products(tabelas["Products"])
tabelas["Sellers"] = tratar_sellers(tabelas["Sellers"])


# Push para o MySQL


print("\n")
print("#" * 70)
print("INICIANDO CARGA PARA O MYSQL")
print("#" * 70)

carregar_tabela(
    tabelas["Customers"],
    "customers"
)

carregar_tabela(
    tabelas["Geolocation"],
    "geolocation"
)

carregar_tabela(
    tabelas["Order Items"],
    "order_items"
)

carregar_tabela(
    tabelas["Order Payments"],
    "order_payments"
)

carregar_tabela(
    tabelas["Order Reviews"],
    "order_reviews"
)

carregar_tabela(
    tabelas["Orders"],
    "orders"
)

carregar_tabela(
    tabelas["Products"],
    "products"
)

carregar_tabela(
    tabelas["Sellers"],
    "sellers"
)

print("\nETL FINALIZADO COM SUCESSO!")


# RELATÓRIO DEPOIS


print("\n")
print("#" * 70)
print("RELATÓRIO APÓS A TRANSFORMAÇÃO")
print("#" * 70)

for nome, df in tabelas.items():
    analisar_dataframe(nome, df)

print("\nPipeline ETL executado com sucesso!")