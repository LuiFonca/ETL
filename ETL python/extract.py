from pathlib import Path
import pandas as pd


# LEITURA DOS CSVs

def carregar_dados():


    base = Path("./dados")

    return {
        "Customers": pd.read_csv(base / "olist_customers_dataset.csv"),
    "Geolocation": pd.read_csv(base / "olist_geolocation_dataset.csv"),
    "Order Items": pd.read_csv(base / "olist_order_items_dataset.csv"),
    "Order Payments": pd.read_csv(base / "olist_order_payments_dataset.csv"),
    "Order Reviews": pd.read_csv(base / "olist_order_reviews_dataset.csv"),
    "Orders": pd.read_csv(base / "olist_orders_dataset.csv"),
    "Products": pd.read_csv(base / "olist_products_dataset.csv"),
    "Sellers": pd.read_csv(base / "olist_sellers_dataset.csv")
    }





