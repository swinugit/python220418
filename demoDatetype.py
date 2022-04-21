#demoDatetype.py

from tkinter import image_types


import time

#print(dir(time))

print(time.time())
#time.sleep(10)
print(time.time())
print(time.gmtime())
print(time.localtime())

from datetime import *
d1 = date.today()
print(d1)
d2 = date(2022, 5, 10)
print(d2)
print(d2-d1)

d3 = datetime.now()
print(d3)
result = str(d3.year) + "/" +str(d3.month) + "/" +str(d3.day)
print(result)

d4 = timedelta(days=100)
print(d1+d4)

import random

print(random.random())
print(random.random())
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))

lotto = list(range(1, 46))
random.shuffle(lotto)
print(lotto)
