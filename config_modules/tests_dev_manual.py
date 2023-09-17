"""Just a sand box to play around with the staff I'm not familiar with.
Not supposed to be used by anybody except me"""

from pydantic_yaml import parse_yaml_raw_as, to_yaml_str
from metadata_classes import PandasColumn,  PandasSchema, PandasDataType
from metadata_classes import EntityTypes
from config import Config,  ConfigET
from config_reader import ConfigReader


def test_read_config():
    print('manual dev testing of config_reader class')
    cr = ConfigReader()
    print(cr.application_config)
    ps = cr.get_orders_pandas_schema()
    print(ps)


def test_read_write_config_classes():
    print('manual dev testing of config  classes')
    etcfs = {EntityTypes.order:
             ConfigET(metadata_file='x', source_data_file='x'),
             EntityTypes.order_item:
             ConfigET(metadata_file="x", source_data_file="x"),
             EntityTypes.order_payment:
             ConfigET(metadata_file='x',  source_data_file='x'),
             EntityTypes.product:
             ConfigET(metadata_file="x", source_data_file="x")}
    conf = Config(input_dir='xxx', output_dir='xxx', metadata_dir='xxx',
                  entity_type_configs=etcfs)
    yml = to_yaml_str(conf)
    print(yml)


def test_read_write_metadata_classes():
    print('manual dev testing of metadata classes')
    m1 = PandasSchema(entity_name='orders', columns=[
         PandasColumn(column_name='order_id',
                      dtype=PandasDataType.date_time, is_in_index=True),
         PandasColumn(column_name='order_status',
                      dtype=PandasDataType.category)])
    # This dumps to YAML and JSON respectively
    yml = to_yaml_str(m1)
    print(yml)
    # jsn = m1.json()

    m2 = parse_yaml_raw_as(PandasSchema, yml)
    assert m1 == m2

    # m3 = parse_yaml_raw_as(pandas_schema, jsn)
    # assert m1 == m3


if __name__ == "__main__":
    # test_read_write_metadata_classes()
    test_read_write_config_classes()
