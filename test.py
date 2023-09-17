import pytest
import pandas as pd

from tests.automation_testing import test_read_orders_df


def test_passed_dummy():
    assert True
    print('passed')


@pytest.mark.skip(reason="test was make to ensure that fails of test work")
def test_failed_dummy():
    assert False, 'shit happens'


def test_read_orders():
    df: pd.DataFrame = test_read_orders_df()
    print(f'{df.shape=} got')
    expected = (24, 5)
    ass_mess = f'{df.shape =} is not correct, expected {expected}'
    assert df.shape == expected, ass_mess
    # 24 rows, 5 columns


#  if __name__ == "__main__":    test_read_orders()
