# ckosche python data getter



## To fetch pages

(do this in root directory of project)

```sh
$ python go.py fetch-firstpages
$ python go.py fetchall
```


## Dev notes

Following instructions are to be run from project root directory:

To run tests:

```sh
$ pytest
```


To run tasks:


```sh
$ python go.py
```







## Random notes

URLs to get:

### $1k to $10k Goal

<$1k Pledged
/discover/advanced?category_id=13&pledged=0&goal=1&sort=newest&seed=2446362&page=1

$1K to $10K pleged

/discover/advanced?category_id=13&pledged=1&goal=1&sort=popularity&seed=2446362&page=1

$10K to $100K pledged
/discover/advanced?category_id=13&pledged=2&goal=1&sort=popularity&seed=2446362&page=1


# Todos

- Organize project directory
- Write scraper of index pages
    - extract project json
    - extract project count
- Write main loop
    - Keep incrementing page number until project count on search page is 0 or returns a 404




# Test code


```py
import json
from pathlib import Path
import src.jks.scrapers.project_scraper as ps
fpath = Path('samples/index-extract-gothamist.json')
txt = fpath.read_text()
data = json.loads(txt)
ps.extract_project(data)
```


```py
from pathlib import Path
import src.jks.scrapers.index_scraper as ix
import src.jks.scrapers.project_scraper as ps
import csv


ipath = Path('samples/index-page-1-of-1.html')
html = ipath.read_text()
pdata = ix.extract_project_data(html)

projects = []
for p in pdata:
  projects.append(ps.extract_project(p))


dest_file = ('samples/index-page-1-of-1.csv')
with open(dest_file, 'w') as w:
   cs = csv.DictWriter(w, fieldnames=list(projects[0].keys()))
   cs.writerows(projects)



```



