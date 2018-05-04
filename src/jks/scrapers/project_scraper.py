from datetime import datetime as dt


def wrangle_project_data(ksdict):
    """
    Args:
        ksdict <dict>:
            A dictionary from parsed JSON representing a KS project, e.g. index-extract-gothamist.json

    Returns:
        <dict>: a dictionary containing the filtered values needed/wanted
    """
    d = {}
    d.update(extract_meta(ksdict))
    d.update(extract_time_fields(ksdict))

    return d


def extract_time_fields(ksdict):
    """
    Args:
        ksdict <dict>:
            A dictionary from parsed JSON representing a KS project, e.g. index-extract-gothamist.json

    Returns:
        <dict>: a dictionary containing the desired converted date values

    Fields to extract/convert:

        "deadline": 1525492740,
        "state_changed_at": 1522728322,
        "created_at": 1521831226,
        "launched_at": 1522728321,

    Extra fields to add:
    """
    d = {}
    d['created_at'] = dt.fromtimestamp(ksdict['created_at']).isoformat()
    return d

def extract_meta(ksdict):
    """
    Extracts:
        - name
        - blurb
        - id
        - photo
        - country
        - url
    """
    d = {}
    d['url'] = ksdict['urls']['web']['project']

    return d
