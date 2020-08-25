#!python

import cgi ,os

form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value
opened_file = open('../post/'+title, 'w')
opened_file.write(description)
print("Location: create.py?id="+title)
print()