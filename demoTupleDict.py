# DemoTupleDict
# Tuple
from doctest import REPORT_UDIFF
import re


tp = (1,2,3)
print(type(tp))
print(tp)
print(len(tp))
print(tp[0])

#주로 데이터를 담아서 전달
#함수를 정의
def calc(a,b):
    return a+b, a*b

#호출

result = calc(3,4)
print(result)

#힌방에 입력
args = (5,6)
print(calc(*args))

#세트는 집합연산

a = {1,2,3,3}
b = {3,4,4,6}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))

#다른 형식으로 변환 튜플을 리스트로 타입캐스팅
a = {1,2,3}
b = list(a)
print(b)
print(type(b))
b.append(4)
print(b)

#딕셔너리
device = {"iphone":5, "ipad" : 10, "wind":20}
print(device)
print(type(device))
print(len(device))
print(device["iphone"])

#입력
device["galaxy"] = 15
device["iphone"] = 6
print(device)

del device["iphone"]
print(device)



