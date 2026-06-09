import pandas as pd



# CUSTOMERS


def tratar_customers(df):
    df = df.drop_duplicates()
    return df



# GEOLOCATION


def tratar_geolocation(df):
    df = df.drop_duplicates()
    return df



# ORDER ITEMS


def tratar_order_items(df):

    df = df.drop_duplicates()

    df["shipping_limit_date"] = pd.to_datetime(
        df["shipping_limit_date"],
        errors="coerce"
    )

    return df



# ORDER PAYMENTS


def tratar_order_payments(df):

    df = df.drop_duplicates()

    return df



# ORDER REVIEWS


def tratar_order_reviews(df):

    df = df.drop_duplicates()

    df["review_comment_title"] = (
        df["review_comment_title"]
        .fillna("Sem título")
    )

    df["review_comment_message"] = (
        df["review_comment_message"]
        .fillna("Sem comentário")
    )

    df["review_creation_date"] = pd.to_datetime(
        df["review_creation_date"],
        errors="coerce"
    )

    df["review_answer_timestamp"] = pd.to_datetime(
        df["review_answer_timestamp"],
        errors="coerce"
    )

    return df



# ORDERS


def tratar_orders(df):

    df = df.drop_duplicates()

    colunas_data = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for coluna in colunas_data:
        df[coluna] = pd.to_datetime(
            df[coluna],
            errors="coerce"
        )

    return df



# PRODUCTS


def tratar_products(df):

    df = df.drop_duplicates()

    df = df.rename(columns={
        "product_name_lenght":
            "product_name_length",

        "product_description_lenght":
            "product_description_length"
    })

    return df



# SELLERS


def tratar_sellers(df):

    df = df.drop_duplicates()

    return df