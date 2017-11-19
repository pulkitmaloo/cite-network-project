# -*- coding: utf-8 -*-
"""
@author: PulkitMaloo
"""

from read_files import read_article, isaac_names
import re


def isValidArticle(article):
    """ Ignore if author is isaac """
    authors = [re.sub(r'[^\w\s]', '', author.lower().strip())
               for author in article["author"].split("and")]
#    print authors
    for isaac_name in isaac_names():
        if isaac_name in authors:
            return False
    return True


for i, article in enumerate(read_article()):
#    print article.keys()
    if not isValidArticle(article):
        print "!!!!! Not valid", i, article["author"]
        continue
