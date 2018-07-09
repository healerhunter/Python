import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('image add').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()
