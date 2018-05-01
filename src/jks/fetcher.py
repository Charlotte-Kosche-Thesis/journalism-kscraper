import jks.indexer as idx
import jks.filer as fil
import requests
from urllib.error import HTTPError

def fetch_index_page(goal, pledged, page):
    """
    If status code is anything but 200, raise an error

    Returns:
        <dict>: the raw HTML as 'text', and other meta information
    """
    url = idx.create_search_url(goal=goal, pledged=pledged, page=page)
    resp = requests.get(url)
    if resp.status_code == 200:
        d = {'text': resp.text, 'url': url, 'goal': goal, 'pledged': pledged, 'page': page }
        return d
    else:
        # https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError
        raise HTTPError(code=resp.status_code, reason=resp.reason, headers=resp.headers)


def fetch_indexes():
    for goal in idx.GOAL_TYPES:
        for pledged in idx.PLEDGE_TYPES:
            for page_num in range(1, 3):
                print("\n")
                print("Goal: {}  Pledge: {}  Page: {}".format(goal, pledged, page_num ))

                dest_path =  fil.generate_index_page_path(goal=goal, pledged=pledged, page=page_num)
                if dest_path.exists():
                    print('\t', 'Already exists:',  dest_path)
                else:
                    print('\t', 'Doesn''t exist:', dest_path)
                    results = fetch_index_page(goal=goal, pledged=pledged, page=page_num)
                    url = results['url']
                    html = results['text']
                    print('\t', 'Downloaded from:', url)
                    print('\t', 'Downloaded chars:', len(html))
                    # now create the directory if needed
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    dest_path.write_text(html)
                    print('\t', 'Saved to:', dest_path)




