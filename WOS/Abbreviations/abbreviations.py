#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Pulkit Maloos)s
"""

from bs4 import BeautifulSoup
import os
import json

outfile = 'abbreviations.txt'

def getfilenames():
    curr_path = os.getcwd()
    files_path = os.path.join(curr_path,'files')
    file_names = ["files/" + fname for fname in os.listdir(files_path)]
    return file_names


def get_dict(rows):
    d = {}
    for i in range(len(rows)//2):
        abbr = rows[2*i+1][1:]
        title = rows[2*i]
        if abbr:
            d[abbr] = title
    return d


def get_list_of_abbr(text):
    soup = BeautifulSoup(text, 'html.parser')
    dt = soup.find("dt").get_text()
    rows = dt.split("\n")[:-1]
    return rows


def parse_files():
    abbreviations = dict()
    for fname in getfilename():
        text = open(fname).read()
        rows = get_list_of_abbr(text)
        abbreviations = {**abbreviations, **get_dict(rows)}
    return abbreviations


def test():
    text = open(getfilenames()[0]).read()
    soup = BeautifulSoup(text, 'html.parser')
    dt = soup.find("dt").get_text()
    rows = dt.split("\n")[:-1]
    for i in range(len(rows)//2):
        abbr = rows[2*i+1][1:]
        title = rows[2*i]
        print(repr(abbr), repr(title))
        break


if __name__ == "__main__":
    abbreviations = parse_files()
    with open(outfile, 'w') as file:
        file.write(json.dumps(abbreviations))

