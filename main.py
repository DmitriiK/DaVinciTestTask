import load_source_data as lsd
from config_modules.metadata_classes import EntityTypes
from aggregate_data import join_dfs


def main_steps():
    df_ord = lsd.get_pandas_dataframe(EntityTypes.order)
    df_ord_itm = lsd.get_pandas_dataframe(EntityTypes.order_item)
    df_joined = join_dfs(df_ord, df_ord_itm)



