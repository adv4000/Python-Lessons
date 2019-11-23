# ------------------------------------------------
# Program by Denis Astahov
#
#
# Version      Date           Info
# 1.0          23-Nov-2019    Initial Version
#
# ----------------------------------------------

from flask import Flask

application = Flask(__name__)


@application.route("/")
def index():
    return "Hello World from Flask Main Page"

@application.route("/help")
def helppage():
    return "<b><font color=blue>This is Help Page v2!!!</font></b>"


@application.route("/user")
def usermain_page():
    return "User's Main Page"


@application.route("/user/<username>")
def show_user_page(username):
    return "Hello " + username.upper()


@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return "SubPath is: " + subpath


@application.route("/kvadrat/<int:x>")
def calc_kvadrat(x):
    return "Kvadrat ot: " + str(x) + " = " + str(x*x)


@application.route("/htmlpage")
def show_html_page():
    myfile = open("mypage.html", mode='r')
    page   = myfile.read()
    myfile.close()
    return page


#--------Main------------------
if __name__ == "__main__":
#    application.debug = True
#    application.env   = "Working Hard"
    application.run()
#------------------------------