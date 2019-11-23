# ------------------------------------------------
# Program by Denis.A.
# 
#
# Version      Date        Info
# 1.0          2016    Initial Version
# Hello Hello
# ------------------------------------------------

mylist = []
msg =""

while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish ")
    mylist.append(msg)

print(mylist)


