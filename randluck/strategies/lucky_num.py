"""
Lucky Number
"""
from typing import List


def get_lucky_nums(num: int) -> List[int]:
    assert num > 0

    taken_num = set()

    curr_num = str(num)
    while len(curr_num) > 1:
        taken_num.update(map(int, curr_num))
        curr_num = str(sum(map(int, curr_num)))

    taken_num.add(int(curr_num))

    lucky_nums = []
    for i in range(9, -1, -1):
        if i not in taken_num:
            lucky_nums.append(i)

    return lucky_nums


def get_lucky_num_from_birth_year(year: int) -> int:
    """Get lucky number by birth year

    Args:
        year (int): Birth year.

    Returns:
        The lucky number (int).

    .. [LuckyNumByBirthYear]: https://zhuanlan.zhihu.com/p/359362331
    """
    assert isinstance(year, int) and year > 0

    lucky_nums = get_lucky_nums(year)
    lucky_num = int("".join(map(str, lucky_nums)))

    return lucky_num
