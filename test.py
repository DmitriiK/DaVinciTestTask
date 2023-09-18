import pytest
from os import path

import etl_modules.load_source_data as lsd
from etl_modules.transform_data import calculate_dfs
from config_modules.metadata_classes import EntityTypes


def test_read_orders_df():
    fn = path.join("tests", "input_data", "olist_orders_dataset.csv")
    print(f'- loading of data from {fn}')
    df = lsd.get_pandas_dataframe(EntityTypes.order, fn)
    print(f'got dataframe with {df.shape=} ')
    expected = (24, 5)  # 24 rows, 5 columns
    ass_mess = f'{df.shape =} is not correct, expected {expected}'
    assert df.shape == expected, ass_mess

    print('- recalculation of week day')
    calculate_dfs(df)
    expected = (24, 6)  # 24 rows, 6 columns
    ass_mess = f'{df.shape =} is not correct, expected {expected}'
    assert df.shape == expected, ass_mess


def test_passed_dummy():
    assert True
    print('passed')


@pytest.mark.skip(reason="test was made to ensure that fails of test work")
def test_failed_dummy():
    assert False, 'shit happens'

#  pytest test.py -s
