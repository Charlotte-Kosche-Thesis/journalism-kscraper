"""
main.py
"""

## relative path hack
# https://stackoverflow.com/a/14999050
import sys
sys.path.insert(0, './src')
##

import argparse
import src.jks.indexer as idx
import src.jks.fetcher as fet
import src.jks.filer as fil

HELP_STRING = """

    Example invocation:

        $ python go.py fetch-index

    Commands:

    hello:
        just a test

    info:
        This message.

    fetch-index:
        Iterate through all the search pages for journalism projects
        and save them to datastash/index-pages

    extract-projects:
        Iterate through the saved pages in datastash/index-pages,
        parse the HTML, and extract the project JSON data and
        save them to datastash/project-data

    status:
        Print the number of index-pages downloaded and projects extracted.

    collate:
        Collate all the project data into a nice CSV file and
        save as datastash/projects.csv

"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run some commands')
    parser.add_argument('command', type=str, nargs='?',
                            help='Print a list of commands', default='info')

    args = parser.parse_args()
    cmd = args.command

    if cmd == 'info':
        print(HELP_STRING)
    elif cmd == 'hello':
        print("Hello world!")
    elif cmd == 'fetch-index':
        print("Fetching the search/index pages")
    else:
        print("The command", cmd, "has not been defined yet...")
