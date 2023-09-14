import pandas as pd


def get_orders():
    source_orders = 'input_data\olist_orders_dataset.csv'

    columns = ["order_id", "order_status", "order_purchase_timestamp"]
    types = {"order_status": "category"}
    df_orders = pd.read_csv(source_orders, header=0,  usecols=columns, dtype=types, parse_dates=[columns[2]])
    df_orders.set_index([columns[0]])
    return df_orders


def get_order_items():
    source_orders = 'input_data\olist_order_items_dataset.csv'
    # order_id	order_item_id product_id	seller_id	shipping_limit_date	price	freight_value
    columns = ["order_id", "order_item_id", "product_id", "price"]
    types = {"order_item_id": "uint8",  "price": "float32"}
    df_orders = pd.read_csv(source_orders, header=0,  usecols=columns, dtype=types, parse_dates=[columns[2]])
    df_orders.set_index(["order_id", "order_item_id"])
    return df_orders


def get_payment():
    source_payments = 'input_data\olist_order_payments_dataset.csv'
    # order_id payment_sequential payment_type payment_installments payment_value 
    columns = ["order_id", "payment_sequential",  "payment_value"]
    types = {"payment_sequential": "uint8",  "payment_value": "float32"}
    df = pd.read_csv(source_payments, header=0, dtype=types, usecols=columns)
    # df_orders.set_index([columns[0], [columns[1]])
    return df


def get_products():
    source_payments = 'input_data\olist_products_dataset.csv'
    # product_id	product_category_name	product_name_lenght	product_description_lenght	product_photos_qty	product_weight_g	product_length_cm	product_height_cm	product_width_cm

    columns = ["product_id", "product_category_name"]
    df = pd.read_csv(source_payments, header=0,  usecols=columns)
    df.set_index([columns[0]])
    return df
