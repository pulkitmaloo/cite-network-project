# -*- coding: utf-8 -*-
"""
@author: PulkitMaloo
"""

from read_files import read_article, isaac_names, abbreviations
import re
import pandas as pd
import re


OUTFILE = "raw_data.xlsx"
ISAAC_NAME = "ISAAC GLYNN"
isaacgl_names = isaac_names()
abbr = abbreviations()


count = 0
errors = 0
success = 0
first = 0
not_first = 0
invalid = 0
mismatch_count = 0
abbr_not_found = []
data = pd.DataFrame()


def isValidArticle(article):
    """ Ignore if author is isaac """
    try:
        authors = [re.sub(r'[^\w\s]', '', author.lower().strip()) \
                   for author in article["author"].split("and")]
    except:
# print("!!!!! Document without author name, title =", article["title"])
        authors = []
    for isaac_name in isaacgl_names:
        if isaac_name in authors:
            return False
    return True


def remove_abbreviations_of_article(article):
    cited_refs = [refs.split(',') for refs in article['cited-references'].split('\n')]
    for i, ref in enumerate(cited_refs):
        for j, info in enumerate(ref):
            if info.strip() in abbr:
                cited_refs[i][j] = " " + abbr[info.strip()]
                break
    return cited_refs


def remove_abbreviations_of_ref(ref):
    flag = True
    for k, info in enumerate(ref):
        info = info.strip()
        if info in abbr:
            ref[k] = " " + abbr[info]
            flag = False
            break

    if flag:
        abbr_not_found.append(ref)
    return ref


def first_author_isaac(article):
    cited_refs = [refs.split(',') for refs in article['cited-references'].split('\n')]
    isaac_refs = []
    temp = []
    for ref in cited_refs:
        author = ref[0].lower().strip()
        author = re.sub(r'[^\w\s]', '', author)

        if author in isaacgl_names:
            temp.append(ref)

        if "isaac" in author:
            global first
            first += 1
            ref = remove_abbreviations_of_ref(ref)
            ref[0] = ISAAC_NAME
            isaac_refs.append(ref)


    if len(isaac_refs) != len(temp):
        global mismatch_count
        mismatch_count += 1
#        print(isaac_refs, "\n", temp, "\n   ++++++ \n")

    return "\n".join([",".join(refs) for refs in isaac_refs])


names = ['issn', 'keywords-plus', 'abstract', 'usage-count-last-180-days',
         'number', 'month', 'affiliation', 'doc-delivery-number', 'year',
         'ENTRYTYPE', 'journal-iso', 'web-of-science-categories', 'title',
         'times-cited', 'unique-id', 'usage-count-since-2013', 'type',
         'author-email', 'journal', 'cited-references', 'da', 'volume',
         'orcid-numbers', 'address', 'ID', 'pages', 'funding-text',
         'publisher', 'doi', 'language', 'keyword',
         'number-of-cited-references', 'author', 'research-areas', 'oa',
         'funding-acknowledgement', 'researcherid-numbers']


for i, article in enumerate(read_article()):
    count += 1
    if not isValidArticle(article):
#        print("!!!!! Isaac cited himself, title:", article["title"],
#              "authors:", article["author"], "\n")
        invalid += 1
        continue
    isaac_refs = first_author_isaac(article)
    if isaac_refs:
        article['cited-references'] = isaac_refs
    else:
        cited_refs = []
        abbr_refs = [refs.split(',') for refs in article['cited-references'].split('\n')]
        for ref in abbr_refs:
            ref = remove_abbreviations_of_ref(ref)
            cited_refs.append(ref)
        article['cited-references'] = "\n".join([",".join(refs) for refs in cited_refs])
    temp = pd.DataFrame(article, index=[0])
    data = pd.concat([data, temp])
    success += 1

writer = pd.ExcelWriter(OUTFILE, engine='xlsxwriter')
data.to_excel(writer, encoding='utf-8', sheet_name='raw-data')

print("=====================================================================")
print("Total", count, "\nSuccess", success, "\nIsaac is First Author", first,
      "\nTitle Abbreviation Encoding not found", len(abbr_not_found), "\nInvalid", invalid)
