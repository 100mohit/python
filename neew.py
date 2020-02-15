import schedule
import time
from datetime import date
import os

# Functions setup

def makefile():

         with open("filename.txt", "w") as f:
           f.write("foo bar")


schedule.every(30).days.at("16:00").do(makefile)

while True:
    # Checks whether a scheduled task
    # is pending to run or not 
    schedule.run_pending()
    time.sleep(1) 