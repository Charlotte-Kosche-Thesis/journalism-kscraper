import jks.indexer as idx
import jks.filer as fil
import jks.scrapers.index_scraper as indexscraper
import requests
from urllib.error import HTTPError
from math import floor

PROJECTS_PER_PAGE = indexscraper.PROJECTS_PER_PAGE


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


def fetch_first_indexpages():
    data = idx.first_pageparams()
    for d in data:
        url = d['url']

        print("Downloading:", url)
        resp = requests.get(url)
        txt = resp.text

        print('\t', 'Downloaded bytes:', len(txt))
        dest_name = fil.generate_indexpage_path(d['goal'], d['pledged'], d['page'])
        dest_name.parent.mkdir(parents=True, exist_ok=True)

        dest_name.write_text(txt)
        print('\t', 'Wrote to:', dest_name)


def statusfoo():
    for fpath in fil.get_all_indexpages():
        txt = fpath.read_text()
        num = indexscraper.extract_project_count(txt)
        print(num, 'projects for', fpath)


def main():
    for fpath in fil.get_first_indexpages():
        print("\n--------------------------------------")
        print(fpath)
        txt = fpath.read_text()
        projnum = indexscraper.extract_project_count(txt)
        pgcount = floor(projnum / PROJECTS_PER_PAGE)
        if pgcount > 0:
            print("\t", 'Total projects:', projnum)
            print("\t", 'Pages to fetch:', pgcount)

            pathmeta = fil.indexpage_path_to_dict(fpath)
            print(pathmeta)

            # we know we have to do second page at this point
            pgnum = 1

            for i in range(pgcount):
                pgnum = pgnum + 1

                src_url = idx.create_search_url(pathmeta['goal'], pathmeta['pledged'], pgnum)
                print('\tDownloading:', src_url)
                resp = requests.get(src_url)
                txt = resp.text

                dest_name = fil.generate_indexpage_path(pathmeta['goal'], pathmeta['pledged'], pgnum)
                print('\tSaving:', dest_name)
                dest_name.write_text(txt)




# def fetch_indexes():
#     for goal in idx.GOAL_TYPES:
#         for pledged in idx.PLEDGE_TYPES:
#             for page_num in range(1, 3):
#                 print("\n")
#                 print("Goal: {}  Pledge: {}  Page: {}".format(goal, pledged, page_num ))

#                 dest_path =  fil.generate_index_page_path(goal=goal, pledged=pledged, page=page_num)
#                 if dest_path.exists():
#                     print('\t', 'Already exists:',  dest_path)
#                 else:
#                     print('\t', 'Doesn''t exist:', dest_path)
#                     results = fetch_index_page(goal=goal, pledged=pledged, page=page_num)
#                     url = results['url']
#                     html = results['text']
#                     print('\t', 'Downloaded from:', url)
#                     print('\t', 'Downloaded chars:', len(html))
#                     # now create the directory if needed
#                     dest_path.parent.mkdir(parents=True, exist_ok=True)
#                     dest_path.write_text(html)
#                     print('\t', 'Saved to:', dest_path)




