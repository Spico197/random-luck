import datetime
import randluck.utils


def test_utc_to_cst():
    utc_datetime = datetime.datetime.utcnow().replace(tzinfo=None)
    cst_datetime = randluck.utils.convert_utc_to_cst(utc_datetime).replace(tzinfo=None)
    timedelta = cst_datetime - utc_datetime
    assert timedelta.seconds == 28800
