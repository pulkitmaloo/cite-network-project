# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 02:34:09 2017

@author: PulkitMaloo
"""

import xml.etree.ElementTree as ET

infile = 'Isaac_Citations_Library.xml'

tree = ET.parse(infile)
root = tree.getroot()
records = root.findall('records/record')
print len(records), "records"

dois = []
titles = []
errors = 0

for record in records:
    try:
#        dois.append(record.find('electronic-resource-num').find('style').text)
        titles.append(record.find('titles').find('title').find('style').text)
    except:
        errors += 1

print len(titles), "titles found"

with open("titles.txt", 'w') as writefile:
    writefile.write('\n'.join(titles).encode('utf-8'))

titles_search = " OR ".join(['TITLE("' + title + '")' for title in titles])

with open('titles_search.txt', 'w') as writefile:
    writefile.write(titles_search.encode('utf-8'))

'''
After running the script above:
* Open `titles_search.txt`.  Copy and paste the search string into Scopus advanced search:
    http://www-scopus-com/search/form.url?zone=TopNavBar&origin=searchadvanced

* Scopus returns 174 results.

* In the search results page, select "Select All", then "View Cited By".

* Scopus returns 911 results.

* Select "Export" > "CSV" and "Specify fields to be exported" > "DOI" only, then "Export".

* Exported file saved as `gen_1 2015-10-30.csv`.
'''