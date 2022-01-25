import datetime

from randluck.strategies.bazi import get_bazi_num_from_utc_datetime
from randluck.strategies.lucky_num import get_lucky_num_from_birth_year


def get_random_seed(utc_datetime=datetime.datetime.utcnow(), strategy="bazi"):
    random_seed = None
    if strategy == "bazi":
        random_seed = get_bazi_num_from_utc_datetime(utc_datetime)
    elif strategy == "lucky_num_by_year":
        random_seed = get_lucky_num_from_birth_year(utc_datetime.year)
    else:
        raise NotImplementedError(f"Unsupported strategy: {strategy}")

    return random_seed
