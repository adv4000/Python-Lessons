# ------------------------------------------------
# Program by Denis.A.
# 
#
# Version      Date        Info
# 1.0          2016    Initial Version
# Hello Hello
# ------------------------------------------------

import re

mytext = "Vasya aaaaaaaa 1972,  Kolya - 19727777: Olesya 1981, aaaaaa@intel.com," \
         "bbbbbbbbbb@intel.com, Petya ggggggggg, 1992,cccccccccc@yahoo.com,  " \
         "ddddddddddd@intel.com, vasya@yandex.net, hello hello, Misha #43 1984, " \
         "Vladimir 1977, Irina , 2001,  annnnnnn@intel.com, eeeeeeee@yandex.com," \
         "ooooooooooo@hotmai.gov, gggggggggggg@gov.gov, tututut@giv.hot"

"""
\d   = Any Digit 0-9
\D   = Any non DIGIT
\w   = Any Alphabet symbol  [A-Z a-z]
\W   = Any non Alphabet symbol
\s   = breakspace
\S   = non breakspace
[0-9]{3}
[A-Z][a-z]+

"""

textlookfor = r"@\w+\.\w+"
allresults = re.findall(textlookfor, mytext)

print(allresults)




