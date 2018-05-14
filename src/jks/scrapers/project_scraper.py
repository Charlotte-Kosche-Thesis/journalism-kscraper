"""
Test code

import src.jks.scrapers.project_scraper as ps
from pathlib import Path
import json


sample_path = Path("samples", "index-extract-gothamist.json")
data = json.loads(sample_path.read_text())

ps.extract_project(data)
"""


from src.jks.helpers import timetostr
import json



def extract_project(kd):
    """
    Args:
        kd <dict>:
            A dictionary from parsed JSON representing a KS project, e.g. index-extract-gothamist.json

    Returns:
        <dict>: a dictionary containing the filtered values needed/wanted
    """
    # rather than do this repetitive code:
    #
    #   d.update(_ext_meta(kd))
    #   ...
    #   d.update(_ext_whatever(kd))
    #
    # ...we make a list containing references to all the extractor functions
    #  so that we can loop through them

    d = {}
    _extractorfoos = [
        _ext_meta,
        _ext_location,
        _ext_time_fields,
        _ext_crowdfunding,
    ]

    for extractor in _extractorfoos:
        try:
            x = extractor(kd)
        except KeyError as err:
            print("oops ValueError", err)
            print(json.dumps(kd, indent=2))
        else:
            d.update(x)




    return d


def _ext_time_fields(kd):
    """
    Args:
        kd <dict>:
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
    d['created_at'] = timetostr(kd['created_at'])
    d['deadline'] = timetostr(kd['deadline'])
    d['launch'] = timetostr(kd['launched_at'])
    return d

def _ext_meta(kd):
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
    d['url'] = kd['urls']['web']['project']
    d['creator_id'] = kd['creator']['id']
    d['creator_name'] = kd['creator']['name']
    d['project_name'] = kd['name']
    d['project_description'] = kd['blurb']
    d['status'] = kd['state']
    d['staff_pick'] = kd['staff_pick']
    return d

def _ext_location(kd):
    d = {}
    _loc = kd.get('location')
    if _loc:
        d['country'] = kd['country']
        d['location_name'] = _loc['displayable_name']
        d['location_slug'] = _loc['slug']
        d['location_type'] = _loc['type']
        d['location_state'] = _loc.get('state')
    return d

def _ext_crowdfunding(kd):
    d = {}
    d['goal'] = kd['goal']
    d['pledged'] = kd['pledged']
    d['percent_funded'] = kd['percent_funded']
    d['currency'] = kd['currency']
    d['backers'] = kd['backers_count']
    return d
