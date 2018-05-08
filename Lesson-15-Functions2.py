# ------------------------------------------------
# Program by Denis.A.
# 
#
# Version      Date        Info
# 1.0          2016    Initial Version
# Hello Hello
# ------------------------------------------------


def create_record(name, telephone, address):
    """Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record


user1 = create_record("Vasya", "+97123123123123123","Tinussiya")
user2 = create_record("Petay", "+64646464646466466","Munisiya")

print(user1)
print(user2)


def give_award(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print("Tovarish " + person.title() + " nagrajdaetsya medaliyu " + medal)


give_award("Za Berlin", "vasya", "petya")
give_award("Za London", "petya", "alexander","valintin")


