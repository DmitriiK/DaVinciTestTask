import pandas as pd

import load_source_data as lsd
from config_modules.metadata_classes import EntityTypes
from config_modules.config_reader import ConfigReader
from transform_data import join_dfs, aggr_df, calculate_dfs
from save_output_data import save_to_parquet


def print_df_data(df: pd.DataFrame):
    print(df.info())
    print(df.shape)
    print(df.head)


def test_read_config():
    cr = ConfigReader()
    print(cr.application_config)


def test_read_df():
    for et in {EntityTypes.order, EntityTypes.order_item}:
        df = lsd.get_pandas_dataframe(et)
        print_df_data(df)


def test_join_df():
    df_ord = lsd.get_pandas_dataframe(EntityTypes.order)
    calculate_dfs(df_ord)
    df_ord_itm = lsd.get_pandas_dataframe(EntityTypes.order_item)
    df = join_dfs(df_ord, df_ord_itm)
    print_df_data(df)
    return df


def test_aggr_df():
    df = test_join_df()
    df_agr = aggr_df(df)
    print_df_data(df_agr)
    return df_agr


def test_save_df():
    df = test_aggr_df()
    save_to_parquet(df)
