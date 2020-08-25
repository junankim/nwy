#!python
print("content-type: text/html; charset=utf-8\n")
import cgi ,os
print("""<!doctype html>
<html>
<head>
  <meta charset = "utf-8">
  

</head>
<body>
  
  <form action = "process_create.py" method = "post">
    <p> <input type = "text" name = "title" placeholder = "title"></p>
    <p><textarea rows = "10" name = "description" placeholder = "description"></textarea></p>
    <p><input type = "submit"></p>
  </form>
  



</body>

</html>""")