"""
Stores, names files
"""
from pathlib import Path
import re


DATA_DIR = Path('datadump')
INDEX_DATA_DIR = Path(DATA_DIR, 'index-pages')

def setup():
    INDEX_DATA_DIR.mkdir(parents=True, exist_ok=True)


def generate_indexpage_path(goal, pledged, page=1):
    goal_dir = 'goal_{}'.format(goal)
    pledge_dir = 'pledged_{}'.format(pledged)
    page_fname = str(page).zfill(3) + '.html'  # pad with 3 zeroes, e.g. 001.html
    dest_path = Path(INDEX_DATA_DIR, goal_dir, pledge_dir, page_fname)
    return dest_path


def indexpage_path_to_dict(fpath):
    fpath = Path(fpath)
    d = {}
    d['path'] = fpath
    d['goal'] = int(re.search(r'goal_\d', str(fpath)).group().split('_')[-1])
    d['pledged'] = int(re.search(r'pledged_\d', str(fpath)).group().split('_')[-1])
    d['page'] = int(fpath.stem)
    return d

def get_first_indexpages():
    return list(INDEX_DATA_DIR.glob('*/**/001.html'))


def get_all_indexpages():
    return list(INDEX_DATA_DIR.glob('goal_*/pledged_*/*.html'))
