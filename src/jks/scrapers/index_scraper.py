from bs4 import BeautifulSoup
import json

PROJECTS_PER_PAGE = 12


def extract_project_count(html):
    """
    From a search/index page, return the project count

    Returns:
        <int>
    """
    soup = BeautifulSoup(html, 'lxml')
    el = soup.select_one('#projects > div.grid-container > h3 > b')
    ptext = el.text  # e.g. "9 projects"
    mystr = ''
    for c in ptext:
        if c.isdigit():
            mystr += c

    num = int(mystr)
    return num

def extract_project_data(html):
    """
    From a search/index page, extract the values of the data-project attributes

    Args:
        html <string>

    Returns:
        <list> of <dict>
    """
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.select('#projects_list > div.grid-row > div')
    projects = []

    for d in divs:
        p = json.loads(d.attrs['data-project'])
        projects.append(p)

    return projects
