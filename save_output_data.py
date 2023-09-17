
import pandas as pd
from dask import dataframe as da

from config_modules.config import Config
from config_modules.config_reader import ConfigReader


def save_to_parquet(df: pd.DataFrame):
    cr = ConfigReader()
    conf: Config = cr.application_config
    df.reset_index(inplace=True)
    ddf = da.from_pandas(df, chunksize=conf.chunk_size)
    ddf.to_parquet(conf.output_dir, partition_on=conf.partitioning_columns,
                   compression=conf.compression)
    # df.to_parquet(conf.output_dir, partition_cols=conf.partitioning_columns)
