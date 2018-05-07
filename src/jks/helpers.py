from datetime import datetime as dt


def timetostr(dval):
    """
    Args:
        dval <datetime>: a datetime object that is timezone naive

    Returns:
        <str> in ISO format in UTC timezone, e.g. '2018-05-05T03:59:00'
    """
    return dt.utcfromtimestamp(dval).isoformat()
