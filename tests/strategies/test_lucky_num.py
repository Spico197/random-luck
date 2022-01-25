from randluck.strategies import lucky_num


def test_get_lucky_num_from_birth_year():
    birth_year = 1997
    num = lucky_num.get_lucky_num_from_birth_year(birth_year)
    assert num == 5430
