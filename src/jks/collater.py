
import csv
from pathlib import Path
import src.jks.filer as filer
import src.jks.scrapers.index_scraper as ix
import src.jks.scrapers.project_scraper as ps



def main():
    projects = []

    for pagepath in filer.get_all_indexpages():
        html = pagepath.read_text()
        kdata = ix.extract_project_data(html)

        for kd in kdata:
            pj = ps.extract_project(kd)
            projects.append(pj)
    return projects



if __name__ == '__main__':
    main()


# ipath = Path('samples/index-page-1-of-1.html')
# html = ipath.read_text()



# dest_file = ('samples/index-page-1-of-1.csv')
# with open(dest_file, 'w') as w:
#    cs = csv.DictWriter(w, fieldnames=list(projects[0].keys()))
#    cs.writeheader()
#    cs.writerows(projects)
