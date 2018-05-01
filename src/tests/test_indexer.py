from jks import indexer


def test_create_search_url():
    url = indexer.create_search_url(goal=1, pledged=2, page=3)
    assert url == 'https://www.kickstarter.com/discover/advanced?category_id=13&sort=newest&goal=1&pledged=2&page=3'


def test_create_search_url_default_page():
    """
    by default, page is set to 1 and is an optional argument
    """
    url = indexer.create_search_url(7, 8)
    assert url == 'https://www.kickstarter.com/discover/advanced?category_id=13&sort=newest&goal=7&pledged=8&page=1'

