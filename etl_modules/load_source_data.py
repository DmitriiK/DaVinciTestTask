import pandas as pd
import os

from config_modules.config_reader import ConfigReader
from config_modules.metadata_classes import PandasDataType,  EntityTypes


def get_pandas_dataframe(et: EntityTypes,
                         src_file_path: str = None) -> pd.DataFrame:
    """_summary_

    Args:
        et (EntityTypes): Entity Type to load, Order, order_item, etc
        src_file_path (str, optional): source file path.
        Defaults to None, -means that path supposed to be taken from config

    Returns:
        pd.DataFrame: pandas dataframe from source file
    """
    cr = ConfigReader()
    conf = cr.application_config
    src_file_name = conf.entity_type_configs[et].source_data_file
    mtd = cr.get_pandas_schema(et)
    source_file_path = (src_file_path or
                        os.path.join(conf.input_dir, src_file_name))
    columns = [x.column_name for x in mtd.columns]
    columns_in_index = [x.column_name for x in mtd.columns if x.is_in_index]
    date_columns = [x.column_name for x in mtd.columns
                    if x.dtype == PandasDataType.date_time]
    excl_dt = [PandasDataType.object, PandasDataType.date_time]
    #  these data types are not supposed to be assigned explicitly
    types = {col.column_name: col.dtype.value
             for col in mtd.columns
             if col.dtype not in excl_dt}
    df = pd.read_csv(source_file_path, header=0,  usecols=columns, dtype=types,
                     parse_dates=date_columns)
    df.set_index(columns_in_index)
    return df
