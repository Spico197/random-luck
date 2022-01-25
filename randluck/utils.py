import pytz
import datetime


def convert_utc_to_cst(utc_datetime: datetime.datetime) -> datetime.datetime:
    return utc_datetime.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Shanghai"))
