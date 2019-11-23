# ------------------------------------------------
# Program by Denis.A.
# 
#
# Version      Date        Info
# 1.0          2016    Initial Version
# Hello Hello
# ------------------------------------------------

#         0     1      2       3        4
cars = ['bmw', 'vw', 'seat', 'skoda', 'kada']

for x in cars:
    print(x.upper())


for x in range(1, 6):
    print(x)

mynumber_list = list(range(0, 10))
print(mynumber_list)
print("===============================================")

for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is: " + str(max(mynumber_list)))
print("Min number is: " + str(min(mynumber_list)))
print("Sum of list is: " + str(sum(mynumber_list)))

print("===============================================")

#         0     1      2       3        4
cars = ['bmw', 'vw', 'seat', 'skoda', 'kada']

mycars = cars[1:4]
print(mycars)
mycars = cars[:4]
print(mycars)

mycars = cars[-3:-1]
print(mycars)


#         0     1      2       3        4
cars = ['bmw', 'vw', 'seat', 'skoda', 'kada']
mycars = cars





