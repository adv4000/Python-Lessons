# ------------------------------------------------
# Program by Denis.A.
# 
#
# Version      Date        Info
# 1.0          2016    Initial Version
# Hello Hello
# ------------------------------------------------

class Hero():
    """ Class to Create Hero for our Game"""
    def __init__(self, name, level, race):
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """ Print all parameters of this Hero"""
        discription = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is " + str(self.health)).title()
        print(discription)

    def level_up(self):
        """ Upgrade Level of Hero"""
        self.level += 1

    def move(self):
        """ Start moving hero"""
        print("Hero " + self.name + " start moving...")

    def set_health(self, new_health):
        self.health = new_health

# ---------------------------------------------------------------------


class SuperHero(Hero):
    """ Class to Crete SUper Hero"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate our Super Hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        """ Use magic"""
        self.magic -= 10

    def show_hero(self):
        discription = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is " + str(self.health) +
                       " Magic is: " + str(self.magic)).title()
        print(discription)

