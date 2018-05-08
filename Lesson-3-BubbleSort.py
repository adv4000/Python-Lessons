# ------------------------------------------------
# Program by Denis.A.
# 
#
# Version      Date        Info
# 1.0          2017    Initial Version
#
# ------------------------------------------------

oldlist = [10, 75, 43, 15, 25, -4, 27]

def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for z in range(0, last_item):
        for x in range(0, last_item-z):
            print(mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]

    return mylist

print("Old List: ", oldlist)
newlist = bubble_sort(oldlist).copy()
print("New List: ", newlist)





