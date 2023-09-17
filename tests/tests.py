import load_source_data as lsd
from config_modules.metadata_classes import EntityTypes
from config_modules.config_reader import ConfigReader


def test_read_config():
    cr = ConfigReader()
    print(cr.application_config)


def test_read_df():
    df = lsd.get_pandas_dataframe(EntityTypes.order)
    print(df.info())

