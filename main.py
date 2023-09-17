import load_source_data as lsd
from config_modules.metadata_classes import EntityTypes
from aggregate_data import join_dfs
from save_output_data import save_to_parquet


def main_steps():
    df_ord = lsd.get_pandas_dataframe(EntityTypes.order)
    df_ord_itm = lsd.get_pandas_dataframe(EntityTypes.order_item)
    df_joined = join_dfs(df_ord, df_ord_itm)
    save_to_parquet(df_joined) 


if __name__ == "__main__":
    # test_read_config()
    main_steps()
