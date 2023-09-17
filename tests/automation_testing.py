from os import path

import etl_modules.load_source_data as lsd
from config_modules.metadata_classes import EntityTypes


def test_read_orders_df():
    et = EntityTypes.order
    fn = path.join("tests", "input_data", "olist_orders_dataset.csv")
    df = lsd.get_pandas_dataframe(et, fn)
    return df
