from pathlib import Path
from requests import Request, Session
from copy import copy

DATA_DIR = Path('datadump')
INDEX_DATA_DIR = Path(DATA_DIR, 'index-pages')
# create subdirectory
INDEX_DATA_DIR.mkdir(parents=True, exist_ok=True)
TEST_DATA_DIR = Path(INDEX_DATA_DIR, 'testing')
TEST_DATA_DIR.mkdir(parents=True, exist_ok=True)

CATEGORY_JOURNALISM = 13
SORT_TYPE='newest'

BASE_ENDPOINT = 'https://www.kickstarter.com/discover/advanced'
BASE_PARAMS = {'category_id': CATEGORY_JOURNALISM, 'sort': SORT_TYPE, 'page': 1}


session = Session()

for i in range(1, 10):
    myparams = copy(BASE_PARAMS)
    myparams['page'] = i
    _r = Request('GET', BASE_ENDPOINT, params=myparams)
    req = _r.prepare()
    print('Getting:', req.url)
    resp = session.send(req)
    html = resp.text
    dest_file = Path(TEST_DATA_DIR, str(i) + '.html')
    dest_file.write_text(html)

    print('Wrote', len(html), 'bytes to:', dest_file)







