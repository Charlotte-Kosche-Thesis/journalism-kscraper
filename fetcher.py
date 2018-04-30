from pathlib import Path
import indexer as idx
import requests

DATA_DIR = Path('datadump')
INDEX_DATA_DIR = Path(DATA_DIR, 'index-pages')
# create subdirectory
INDEX_DATA_DIR.mkdir(parents=True, exist_ok=True)
for goal in idx.GOAL_TYPES:
    for page_num in range(1, 10):
        url = idx.create_search_url(goal=goal, page=page_num)
        print('Getting:', url)
        # resp = requests.get(url)
        # html = resp.text
        
        dest_file = Path(TEST_DATA_DIR, str(i) + '.html')
        # dest_file.write_text(html)

        print('Wrote', len(html), 'bytes to:', dest_file)







