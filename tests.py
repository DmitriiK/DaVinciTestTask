import load_source_data as lsd
from config_modules.metadata_classes import EntityTypes

df = lsd.get_pandas_dataframe(EntityTypes.order)
print(df.info())