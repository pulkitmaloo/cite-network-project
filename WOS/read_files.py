# -*- coding: utf-8 -*-
"""
@author: PulkitMaloo
"""
import bibtexparser


def getfilename():
    for i in range(39):
        yield "files/savedrecs (" + str(i) + ").bib"


def read_bibtex(fname):
    with open(fname, "r") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database


def read_file():
    for fname in getfilename():
        try:
            bib_db = read_bibtex(fname)
            print "Successfuly read " + str(len(bib_db.entries)) + \
                  " articles from", fname
            yield bib_db.entries
        except:
#            print "file not found:", fname
            pass


def read_article():
    for articles in read_file():
        for article in articles:
            yield article


def isaac_names():
    fname = "Isaac_Search.txt"
    try:
        with open(fname, "r") as fhand:
            names_str = fhand.read().strip().lower()
        return [n.strip() for n in names_str.split("or")]
    except:
        print "File not found:", fname

if __name__ == "__main__":
    for x in read_article():
        pass
    print isaac_names()