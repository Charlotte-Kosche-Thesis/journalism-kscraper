# ckosche python data getter



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
