import indexer as idx
import filer as fil
import requests


def go():
    pledged = '' # just ignoring pledged for now
    for goal in idx.GOAL_TYPES:
        for page_num in range(1, 10):
            print("\n")
            print("Goal: {}  Pledge: {}  Page: {}".format(goal, pledged, page_num ))
            dest_path =  fil.generate_index_page_path(goal=goal, page=page_num)
            if dest_path.exists():
                print('\t', 'Already exists:',  dest_path)
            else:
                print('\t', 'Doesn''t exist:', dest_path)
                url = idx.create_search_url(goal=goal, page=page_num)
                print('\t', 'Downloading:', url)

                resp = requests.get(url)
                if resp.status_code == 200:
                    html = resp.text
                    print('\t', 'Downloaded chars:', len(html))
                    
                    # now create the directory if needed
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    dest_path.write_text(html)
                    print('\t', 'Saved to:', dest_path)

                





if __name__ == '__main__':
    go()



