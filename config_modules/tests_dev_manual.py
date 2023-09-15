
from pydantic_yaml import parse_yaml_raw_as, to_yaml_str
from metadata_classes import PandasColumn,  PandasSchema, PandasDataType
from config_modules.config_reader import ConfigReader


def test_read_config():
    print('manual dev testing of config_reader class')
    cr = ConfigReader()
    print(cr.application_config)
    ps = cr.get_orders_pandas_schema()
    print(ps)


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
    test_read_write_metadata_classes()
