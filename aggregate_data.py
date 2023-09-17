import load_source_data as lsd
import pandas as pd

from config_modules.metadata_classes import EntityTypes

"""some metadata related constants, that can be potentially
    became parameters or configurables in the future"""
date_col = 'order_purchase_timestamp'
week_col = 'date_week_begin'
gr_by_cols = ['date_week_begin', "product_id"]  # columns to group by
aggr = ('price', 'sum')  # aggregation definitions
gr_by_cols = ['date_week_begin', "product_id"]  # columns to group by
prt_by_cols = ["product_id"]  # columns for partitioning


def join_dfs() -> pd.DataFrame:
    df_ord = lsd.get_pandas_dataframe(EntityTypes.order)
    df_ord[week_col] = (df_ord[date_col] - pd.to_timedelta
                        (df_ord[date_col].dt.dayofweek, unit='D')).dt.date
    # by elimination of time here we are loosing date data type..
    df_ord_itm = lsd.get_pandas_dataframe(EntityTypes.order_item)
    df_common = pd.merge(df_ord, df_ord_itm)
    df_aggr = df_common.groupby(gr_by_cols).agg(sum_sales=aggr)
    return df_aggr


# df_aggr.to_parquet("./output", partition_cols=['product_category_name'])
