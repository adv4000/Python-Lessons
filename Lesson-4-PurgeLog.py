#!/bin/python3
# ------------------------------------------------
# Program by Denis.A.
# 
#
# Version      Date        Info
# 1.0          2017    Initial Version
#
# ------------------------------------------------

import shutil    # For CopyFile
import os        # For GetFileSize  and  Check If File exist
import sys       # For CLI  Arguments

# lesson-4-putgelog.py  mylog.txt  10  5

if(len(sys.argv) < 4):
    print("Missing arguments!  Usage is script.py  mylog.txt 10  5")
    exit(1)

file_name  = sys.argv[1]
limitsize  = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):           # Check if MAIN logfile file exist
    logfile_size = os.stat(file_name).st_size    # Get Filesize in BYTES
    logfile_size = logfile_size / 1024           # Convert from BYTES to KILOBYTES

    if(logfile_size >= limitsize):
        if(logsnumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):
                src = file_name + "_" + str(currentFileNum-1)
                dst = file_name + "_" + str(currentFileNum)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
                    print("Copied: " + src + " to " + dst)

            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + file_name + "   to " + file_name + "_1")
        myfile = open(file_name, 'w')
        myfile.close()

