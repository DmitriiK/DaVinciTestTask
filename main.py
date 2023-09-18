
"""Main module of the application.
`  Has date_column name  as command line argument
     example of command line call :
    - > python main.py --date_column order_approved_at
    """

import argparse

import etl_modules.load_source_data as lsd
from config_modules.metadata_classes import EntityTypes
from etl_modules.transform_data import calculate_dfs, join_dfs, aggr_df
from etl_modules.save_output_data import save_to_parquet


dc_help_str = """One of possible date attributes for group by.
                    Kind of role-playing date dimension."""
parser = argparse.ArgumentParser()
parser.add_argument("--date_column", type=str, help=dc_help_str,
                    nargs='?',
                    choices=['order_purchase_timestamp',
                             'order_approved_at',
                             'order_delivered_customer_date'],
                    default='order_purchase_timestamp')


def main_steps():
    args = parser.parse_args()
    date_column = args.date_column
    df_ord = lsd.get_pandas_dataframe(EntityTypes.order)
    calculate_dfs(df_ord, date_column)  # added calc. columns
    df_ord_itm = lsd.get_pandas_dataframe(EntityTypes.order_item)
    df_joined = join_dfs(df_ord, df_ord_itm)
    df_aggregated = aggr_df(df_joined)
    save_to_parquet(df_aggregated)


if __name__ == "__main__":
    main_steps()
