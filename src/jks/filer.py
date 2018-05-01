from pathlib import Path

DATA_DIR = Path('datadump')
INDEX_DATA_DIR = Path(DATA_DIR, 'index-pages')

def setup():
    INDEX_DATA_DIR.mkdir(parents=True, exist_ok=True)


def generate_index_page_path(goal, pledged, page=1):
    goal_dir = 'goal_{}'.format(goal)
    pledge_dir = 'pledged_{}'.format(pledged)
    page_fname = str(page).zfill(3) + '.html'  # pad with 3 zeroes, e.g. 001.html
    dest_path = Path(INDEX_DATA_DIR, goal_dir, pledge_dir, page_fname)
    return dest_path


