import load_source_data as lsd
import pandas as pd


df_orders = lsd.get_orders()
date_column = 'order_purchase_timestamp'
df_orders['date_week_begin'] = (df_orders[date_column] - pd.to_timedelta(df_orders[date_column].dt.dayofweek, unit='D')).dt.date
# note - by elimination of time here we are loosing date data type, getting object..

print(df_orders.info())
print(df_orders)

df_oi = lsd.get_order_items()
print(df_oi.info())
print(df_oi)

df_pr = lsd.get_products()
print(df_pr.info())
print(df_pr)

df_common = pd.merge(df_orders, pd.merge(df_oi, df_pr))

print(df_common.info())
print(df_common.head())

df_aggr = df_common.groupby(["product_category_name",  'date_week_begin',"product_id"]).agg(sum_sales=('price', 'sum'))

print(df_aggr.info())
print(df_aggr.head(100))
df_aggr.to_parquet("./output", partition_cols=['product_category_name'])




