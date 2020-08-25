#!python
print("content-type: text/html; charset=utf-8\n")
import cgi ,os

files = os.listdir('../post')
listStr = ""
for item in files : 
  listStr = listStr + '<li><a href = "index.py?id={name}">{name}</a></li>'.format(name = item)

form = cgi.FieldStorage()
if "id" in form:
    pageId = form ["id"].value
    description = open("../post/"+pageId,'r').read()
else :
    pageId = "welcome"
    description = 'Hello,web'

print("""<!doctype html>
<html>
<head>
  <meta charset = "utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
  <h1><a href = "yongeeks.html">Yongeeks</a></h1>
  <ol>
   {listStr}

  </ol>
  
  <button type="button" onclick="location.href='write.py' ">write</button>

  
  



</body>

</html>""".format(listStr = listStr))