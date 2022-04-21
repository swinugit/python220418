#demoOS.py

from os.path import *

print(abspath("python.exe"))
#print(basename("/Users/seo/Desktop/work/python.exe"))
#print(getsize("/Users/seo/Desktop/work/python.exe"))
#print(exists("/Users/seo/Desktop/work/python.exe"))
#print(isfile("/Users/seo/Desktop/work/python.exe"))

#운영체제 정보
from os import *
print("운영체제이름:", name)
#다른 실행파일 실행
#system("notepad.exe")

import glob
print(glob.glob("/Users/seo/Desktop/work/*.py"))