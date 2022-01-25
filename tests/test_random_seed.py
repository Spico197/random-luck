import datetime
from collections import namedtuple

import pytest

import randluck


def test_get_random_seed_lucky_num_birth():
    random_seed = randluck.get_random_seed(
        utc_datetime=datetime.date(year=1997, month=1, day=1),
        strategy="lucky_num_by_year",
    )
    assert random_seed == 5430


def test_get_none_random_seed_lucky_num_birth():
    date = namedtuple("date", ["year"])

    with pytest.raises(AssertionError):
        date.year = 0
        randluck.get_random_seed(utc_datetime=date, strategy="lucky_num_by_year")

    for year in range(1, 10000):
        date.year = year
        random_seed = randluck.get_random_seed(
            utc_datetime=date, strategy="lucky_num_by_year"
        )
        assert random_seed is not None


def test_none_strategy():
    with pytest.raises(NotImplementedError):
        randluck.get_random_seed(strategy=None)


def test_bazi_random_num():
    now_datetime = datetime.datetime(2022, 1, 25, 8, 15, 39, 849134)
    num = randluck.get_random_seed(utc_datetime=now_datetime)
    assert num == 64117
