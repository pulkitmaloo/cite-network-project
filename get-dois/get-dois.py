# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 02:34:09 2017

@author: PulkitMaloo
"""

import xml.etree.ElementTree as ET

infile = 'Isaac_Citations_Library.xml'
search_string_outfile = 'titles_search.txt'

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

titles_search = " OR ".join(['TITLE("' + title + '")' for title in titles])

with open(search_string_outfile, 'w') as writefile:
    writefile.write(titles_search.encode('utf-8'))
