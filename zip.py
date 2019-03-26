#this program is created to compress the split file into one zip
# if required
from zipfile import *
f = ZipFile('compressed.zip','w',ZIP_DEFLATED)
f.write('hack1.nitesh')
f.write('hack2.intel')
f.close()