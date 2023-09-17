"""module is responsible for transforming part in kind of ETL"""
import pandas as pd

"""some metadata related constants, that can potentially
    became parameters or configirable in the future"""
week_col = 'date_week_begin'
gr_by_cols = ['product_id', "date_week_begin"]  # columns to group by
aggr = ('price', 'sum')  # aggregation definitions
gr_by_cols = ['date_week_begin', "product_id"]  # columns to group by


def calculate_dfs(df_ord: pd.DataFrame,
                  date_col: str = 'order_purchase_timestamp') -> pd.DataFrame:
    """_summary_

    Args:
        df_ord (pd.DataFrame): pandas dataframe where we
         want to add some calculated columns
        date_col (str, optional): Name of column related to main date
        attribute for reporting. Defaults to ''.

    Returns:
        pd.DataFrame: same df, enriched with calculations
    """
    # if arg_date_col:        date_col = arg_date_col
    df_ord[week_col] = (df_ord[date_col] - pd.to_timedelta
                        (df_ord[date_col].dt.dayofweek, unit='D')).dt.date
    # by elimination of time here we are loosing date data type..


def join_dfs(df_ord: pd.DataFrame, df_ord_itm: pd.DataFrame) -> pd.DataFrame:
    """just join of dfs.. here should be smth more complex in the future"""
    df_joined = pd.merge(df_ord, df_ord_itm)
    return df_joined


def aggr_df(df: pd.DataFrame) -> pd.DataFrame:
    df_aggr = df.groupby(gr_by_cols).agg(sum_sales=aggr)
    return df_aggr
