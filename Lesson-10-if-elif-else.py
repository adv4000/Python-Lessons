# ------------------------------------------------
# Program by Denis.A.
# 
#
# Version      Date        Info
# 1.0          2016    Initial Version
# Hello Hello
# ------------------------------------------------

age = 14

if (age <= 4):
    print("You are baby!")
elif (age > 4) and (age < 12):
    print("You age kid")
elif (age >= 12) and (age < 19):
    print("You age teenager")
else:
    print("You are old!")

print("----END----")


all_cars = ['chrusler', 'dacia', 'bmw', 'KIA', 'vw', 'seat', 'skoda', 'lada', 'audi', 'ford', 'Chevrolett']
german_cars = ['bmw', 'vw', 'audi']


for xxxx in all_cars:
    if xxxx not in german_cars:
        print(xxxx + " is not German Car" + " index = " + str(all_cars.index(xxxx)))






