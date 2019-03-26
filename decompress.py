# this progress is created for to decompress the
# compressed file
from zipfile import *
f = ZipFile('compressed.zip','r')
f.extractall()