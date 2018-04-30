from urllib.parse import urlencode
from copy import copy
# https://www.kickstarter.com/discover/advanced?category_id=13&sort=newest&goal=0&page=1


BASE_ENDPOINT = 'https://www.kickstarter.com/discover/advanced'
CATEGORY_JOURNALISM = 13
SORT_TYPE='newest'

GOAL_TYPES = [0, 1, 2, 3, 4]
PLEDGE_TYPES = [0, 1, 2, 3, 4]

BASE_PARAMS = { 'category_id': CATEGORY_JOURNALISM, 
                       'sort': SORT_TYPE }


def create_search_url(goal, pledged="", page=1, ):
    myparams = copy(BASE_PARAMS)
    myparams['goal'] = goal    
    myparams['page'] = page
    if pledged is not '':
        myparams['pledged'] = pledged
    url = BASE_ENDPOINT + '?' + urlencode(myparams)
    return url



# def create_goal_urls():
#     urls = []
#     for g in GOAL_TYPES:
#         u = create_search_url(goal=g)
#         urls.append(u)
#     return urls



