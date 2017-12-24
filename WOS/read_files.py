# -*- coding: utf-8 -*-
"""
@author: PulkitMaloo
"""
import bibtexparser
import json
import os


def getfilename():
    curr_path = os.getcwd()
    files_path = os.path.join(curr_path,'files')
    file_names = ["files/" + fname for fname in os.listdir(files_path)]
    return file_names


def read_bibtex(fname):
    with open(fname, "r") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
        return bib_database


def read_file():
    for fname in getfilename():
        if "saved" not in fname:
            continue
        bib_db = read_bibtex(fname)
#        print("Read", len(bib_db.entries), "articles from", fname)
        yield bib_db.entries


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
        print("File not found:", fname)


def abbreviations():
    fname = "Abbreviations/abbreviations.txt"
    try:
        with open(fname, "r") as fhand:
            abbr = json.loads(fhand.read())
            return abbr
    except:
        print("File not found:", fname)


if __name__ == "__main__":
    for x in read_article():
        pass
#    print isaac_names()