#In this program your file is splited into two part(file)
# the extension of both the file is different and binary
#  pattern are also changed
f1 = open('applet-lifecycle.jpg','rb')
f2 = open('hack1.nitesh','wb')
f3 = open('hack2.intel','wb')
bytes = f1.read()
f2.write(bytes[len(bytes)//2::-1])
f3.write(bytes[:len(bytes)//2:-1])
f1.close()
f2.close()
f3.close()

