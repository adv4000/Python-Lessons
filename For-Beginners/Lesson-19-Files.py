# ------------------------------------------------
# Program by Denis.A.
# 
#
# Version      Date        Info
# 1.0          2016    Initial Version
# Hello Hello
# ------------------------------------------------


inputfile = "../list_of_password.txt"
outputfile = "../my_passwords.txt"

password_tolookfor = "kolya"

myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='a', encoding='latin_1')

for num, line in enumerate(myfile1, 1):
    if password_tolookfor in line:
        print("Line N: " + str(num) + " : " + line.strip())
        myfile2.write("Found password:" + line)


myfile1.close()
myfile2.close()








