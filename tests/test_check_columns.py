#!/usr/bin/env python3
from pl_curve import check_columns
import pandas
import pytest

@pytest.mark.parametrize('dataframe', [pandas.DataFrame([1.0, 0, 0, 0]), 
pandas.DataFrame([0.1, 0.4, 0.2, 0.3])])
def test_check_columns_correct(dataframe):
    '''FIXME: Implement this test
    Tests check_columns correctly checks items summing to 1.0 returns true
    '''
    assert check_columns(dataframe) is True
    #raise NotImplementedError("Please implement this test")

def test_check_columns_incorrect():
    df = pandas.DataFrame([0.1, 0.8])
    assert check_columns(df) is False
