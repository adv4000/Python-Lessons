# ------------------------------------------------
# Program by Denis.A.
# 
#
# Version      Date        Info
# 1.0          2016    Initial Version
# Hello Hello
# ------------------------------------------------
import sys

filename = "Lesson_List.txt"

while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding="Latin-1")
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        print(sys.exc_info()[1])
        filename = input("ENter Correct file name! :")
    else:
        print("Indise ELSE")
        print(myfile.read())
        break


print("======================EOF================")

