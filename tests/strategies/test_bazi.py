import datetime

from randluck.strategies import bazi


def test_get_bazi_num():
    now_datetime = datetime.datetime(2022, 1, 25, 8, 15, 39, 849134)
    num = bazi.get_bazi_num_from_utc_datetime(now_datetime)
    assert num == 64117


def test_get_bazi():
    bazi_nums = bazi.get_bazi_nums(datetime.datetime(2021, 1, 25, 15))
    assert bazi_nums == [6, 0, 5, 1, 9, 9, 6, 8]

    bazi_string = bazi.convert_bazi_nums_to_string(bazi_nums)
    assert bazi_string == "庚子己丑癸酉庚申"

    bazi_converted_nums = bazi.convert_bazi_string_to_nums("庚子己丑癸酉庚申")
    assert bazi_converted_nums == bazi_nums
