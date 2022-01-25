import datetime
from typing import List

import sxtwl

from randluck.utils import convert_utc_to_cst
from randluck.strategies.lucky_num import get_lucky_nums


Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]


def convert_bazi_nums_to_string(bazi_nums: List[int]) -> str:
    assert isinstance(bazi_nums, list)
    assert any(map(lambda x: isinstance(x, int), bazi_nums))

    ganzhi_string = ""
    i = 0
    while i < len(bazi_nums):
        tiangan = Gan[bazi_nums[i]]
        dizhi = Zhi[bazi_nums[i + 1]]
        ganzhi_string += f"{tiangan}{dizhi}"
        i += 2
    return ganzhi_string


def convert_bazi_string_to_nums(bazi_string: str) -> List[int]:
    assert isinstance(bazi_string, str)
    assert len(bazi_string) > 0
    assert len(bazi_string) % 2 == 0

    bazi_nums = []
    i = 0
    while i < len(bazi_string):
        gan_idx = Gan.index(bazi_string[i])
        zhi_idx = Zhi.index(bazi_string[i + 1])
        bazi_nums.extend([gan_idx, zhi_idx])
        i += 2

    return bazi_nums


def get_bazi_nums(cst_time: datetime.datetime) -> List[int]:
    assert isinstance(cst_time, datetime.datetime)

    bazi = []
    lunar_info = sxtwl.fromSolar(cst_time.year, cst_time.month, cst_time.day)

    # Ganzhi year in Bazi starts from Lichun
    year_ganzhi = lunar_info.getYearGZ(False)
    bazi.extend([year_ganzhi.tg, year_ganzhi.dz])
    month_ganzhi = lunar_info.getMonthGZ()
    bazi.extend([month_ganzhi.tg, month_ganzhi.dz])
    day_ganzhi = lunar_info.getDayGZ()
    bazi.extend([day_ganzhi.tg, day_ganzhi.dz])
    hour_ganzhi = lunar_info.getHourGZ(cst_time.hour)
    bazi.extend([hour_ganzhi.tg, hour_ganzhi.dz])

    return bazi


def get_bazi_num_from_utc_datetime(utc_datetime=datetime.datetime.utcnow()) -> int:
    assert isinstance(utc_datetime, datetime.datetime)

    cst_time = convert_utc_to_cst(utc_datetime)
    bazi_nums = get_bazi_nums(cst_time)
    lucky_nums = get_lucky_nums(utc_datetime.day)
    # take only the last 6 to prevent overflowed number
    lucky_nums = list(filter(lambda x: 0 <= x < 8, lucky_nums))[-6:]

    bazi_nums_revised = []
    for i in lucky_nums:
        bazi_nums_revised.append(bazi_nums[i])

    bazi_joint_result = int("".join(map(str, bazi_nums_revised)))
    return bazi_joint_result
