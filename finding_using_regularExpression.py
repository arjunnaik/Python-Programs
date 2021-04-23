import os
import shutil


os.chdir("D:\SQL Work")

shutil.copy("D:\SQL Work\SQL-Code.txt", "D:\DB Lab")

import re

findnumberregex = re.compile(r"\d{10}")
findemailregex = re.compile(r"[a-zA-Z0-9]+@gmail.com")
str = "9900161007 arjun123@gmail.com 7972957143 arjunvnaik31@gmail.com"
number = findnumberregex.findall(str)
email = findemailregex.findall(str)
print(number)
print(email)