from urllib import request

myUrl = "http://www.astahov.net"

otvet = request.urlopen(myUrl)
mytext1 = otvet.readlines()
#mytext2 = otvet.read()
#print(otvet)

#print(mytext2)

for line in mytext1:
    print(str(line).lstrip("b'").rstrip("\\r\\n'"))



