from urllib import request
import sys


myUrl = "http://adv400.tripod.com/kartinka.jpg"
myFile = "G:\\MyPython\\MyDownloads\\mykartinka.jpg"

try:
        print("Start Downloading file from: " + myUrl)
        request.urlretrieve(myUrl, myFile)
except Exception:
    print("AHTUNG!!!")
    print(sys.exc_info())
    exit

print("File Downloaded and saved at:" + myFile)
