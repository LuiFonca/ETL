from mysql_explorer import carregar_tabela_mysql


def total_clientes():

    df = carregar_tabela_mysql(
        "customers"
    )

    return len(df)


def total_pedidos():

    df = carregar_tabela_mysql(
        "orders"
    )

    return len(df)


def total_produtos():

    df = carregar_tabela_mysql(
        "products"
    )

    return len(df)


def total_vendedores():

    df = carregar_tabela_mysql(
        "sellers"
    )

    return len(df)


def total_reviews():

    df = carregar_tabela_mysql(
        "order_reviews"
    )

    return len(df)


def total_geolocations():

    df = carregar_tabela_mysql(
        "geolocation"
    )

    return len(df)


def valor_total_vendido():

    df = carregar_tabela_mysql(
        "order_payments"
    )

    return round(
        df["payment_value"].sum(),
        2
    )


def ticket_medio():

    df = carregar_tabela_mysql(
        "order_payments"
    )

    return round(
        df["payment_value"].mean(),
        2
    )


def nota_media_reviews():

    df = carregar_tabela_mysql(
        "order_reviews"
    )

    return round(
        df["review_score"].mean(),
        2
    )


def pagamento_mais_utilizado():

    df = carregar_tabela_mysql(
        "order_payments"
    )

    return (
        df["payment_type"]
        .value_counts()
        .idxmax()
    )