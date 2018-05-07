from jks import helpers as hp
from datetime import datetime
import pytz
import re

# https://stackoverflow.com/questions/24856643/unexpected-results-converting-timezones-in-python

PST_TZ = pytz.timezone('US/Pacific')
# i.e. Dec. 30, 1999, at 11:08:59 PM, Pacific time
THE_TIME = datetime(1999, 12, 30, 23, 8, 59, tzinfo=PST_TZ)
#   i.e. Dec. 31, 1999; 07:08:59 AM, UTC

def test_timetostr_returns_iso_format():
    tstamp = THE_TIME.timestamp()
    dt = hp.timetostr(tstamp)
    assert type(dt) is str
    assert '1999-12-31' in dt
    assert '07:08:59' in dt
