import pandas as pd
import os

from config_modules.config_reader import ConfigReader
from config_modules.metadata_classes import PandasDataType,  EntityTypes


def get_pandas_dataframe(et: EntityTypes) -> pd.DataFrame:
    cr = ConfigReader()
    conf = cr.application_config
    mtd = cr.get_pandas_schema(et)
    source_file_path = os.path.join(conf.input_dir, mtd.file_name)
    columns = [x.column_name for x in mtd.columns]
    columns_in_index = [x.column_name for x in mtd.columns if x.is_in_index]
    date_columns = [x.column_name for x in mtd.columns
                    if x.dtype == PandasDataType.date_time]
    excl_dt = [PandasDataType.object, PandasDataType.date_time]
    #  these data types are not supposed to be assigned explicitely 
    types = {col.column_name: col.dtype.value
             for col in mtd.columns
             if col.dtype not in excl_dt}
    df = pd.read_csv(source_file_path, header=0,  usecols=columns, dtype=types,
                     parse_dates=date_columns)
    df.set_index(columns_in_index)
    return df

