import pandas as pd

from mysql_explorer import (
    carregar_tabela_mysql
)


def pagamentos_por_tipo():

    df = carregar_tabela_mysql(
        "order_payments"
    )

    return (
        df["payment_type"]
        .value_counts()
    )


def pedidos_por_estado():

    orders = carregar_tabela_mysql(
        "orders"
    )

    customers = carregar_tabela_mysql(
        "customers"
    )

    df = orders.merge(
        customers,
        on="customer_id"
    )

    return (
        df["customer_state"]
        .value_counts()
        .head(10)
    )