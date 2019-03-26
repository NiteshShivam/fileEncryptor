# this program is created for to get back the
# original fie
f1 = open('hack1.nitesh','rb')
f2 = open('hack2.intel','rb')
f3 = open('trail.mp3','ab+')
b1 = f1.read()
b2 = f2.read()
b1 = b1[::-1]
b2 = b2[::-1]
f3.write(b1)
f3.write(b2)
f1.close()
f2.close()
f3.close()