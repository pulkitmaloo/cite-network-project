# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 02:34:09 2017

@author: PulkitMaloo
"""

import xml.etree.ElementTree as ET
import csv

infile = 'Isaac_Citations_Library.xml'
outfile = 'Isaac_Citations_Library.csv'


def read_file_as_dict(fname):
    import xmltodict
    with open(infile,"r") as fhand:
        xml_str = fhand.read()
    xdict = xmltodict.parse(xml_str)
    return xdict["xml"]["records"]["record"]


def read_file_as_xml(fname):
    tree = ET.parse(infile)
    root = tree.getroot()
    records = root.findall('records/record')
    print(len(records), "records found")
    return records


def parse_records_as_xml(records):
    for i, record in enumerate(records):
        count = 0


if __name__=="__main__":
    records = read_file_as_xml(infile)
    parse_records_as_xml(records)



#dois = []
#titles = []
#errors = 0
#
#for record in read_file(infile):
#    try:
##        dois.append(record.find('electronic-resource-num').find('style').text)
#        titles.append(record.find('titles').find('title').find('style').text)
#    except:
#        errors += 1
#
#print len(titles), "titles found"
#
#with open("titles.txt", 'w') as writefile:
#    writefile.write('\n'.join(titles).encode('utf-8'))
#
#titles_search = " OR ".join(['TITLE("' + title + '")' for title in titles])
#
#with open('titles_search.txt', 'w') as writefile:
#    writefile.write(titles_search.encode('utf-8'))

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