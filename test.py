import pytest
from os import path

import etl_modules.load_source_data as lsd
from config_modules.metadata_classes import EntityTypes


def test_read_orders_df():
    et = EntityTypes.order
    fn = path.join("tests", "input_data", "olist_orders_dataset.csv")
    df = lsd.get_pandas_dataframe(et, fn)
    print(f'{df.shape=} got')
    expected = (24, 5)
    ass_mess = f'{df.shape =} is not correct, expected {expected}'
    assert df.shape == expected, ass_mess
    # 24 rows, 5 columns


def test_passed_dummy():
    assert True
    print('passed')


@pytest.mark.skip(reason="test was make to ensure that fails of test work")
def test_failed_dummy():
    assert False, 'shit happens'
