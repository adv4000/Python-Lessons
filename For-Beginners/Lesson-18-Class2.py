# ------------------------------------------------
# Program by Denis.A.
# 
#
# Version      Date        Info
# 1.0          2016    Initial Version
# Hello Hello
# ------------------------------------------------


from hero import *


myhero = Hero("Vurdalak", 4, "Orc")
mysuperhero = SuperHero("Moisey", 10, "Human", 5)

myhero.show_hero()
mysuperhero.show_hero()

mysuperhero.makemagic()
mysuperhero.show_hero()

mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.show_hero()


mysuperhero.magic = 10
mysuperhero.show_hero()

