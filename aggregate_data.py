import pandas as pd

"""some metadata related constants, that can potentially
    became parameters or configurables in the future"""
date_col = 'order_purchase_timestamp'
week_col = 'date_week_begin'
gr_by_cols = ['product_id', "date_week_begin"]  # columns to group by
aggr = ('price', 'sum')  # aggregation definitions
gr_by_cols = ['date_week_begin', "product_id"]  # columns to group by


def join_dfs(df_ord: pd.DataFrame, df_ord_itm: pd.DataFrame) -> pd.DataFrame:
    df_ord[week_col] = (df_ord[date_col] - pd.to_timedelta
                        (df_ord[date_col].dt.dayofweek, unit='D')).dt.date
    # by elimination of time here we are loosing date data type..
    df_joined = pd.merge(df_ord, df_ord_itm)
    return df_joined


def aggr_df(df: pd.DataFrame) -> pd.DataFrame:
    df_aggr = df.groupby(gr_by_cols).agg(sum_sales=aggr)
    return df_aggr
