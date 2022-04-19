# ifelse.py
#다중라인 주석처리: 윈도우 CTR / , 맥: command /
# score = int(input("score input:"))

# if 90 <= score <=100:
#     grade = "A"
# elif 80 <= score <90:
#     grade = "B"
# elif 70<= score <80:
#     grade = "c"
# else:
#     grade = "D"

# print("grade", grade)

value = 5
while value > 0:
    print(value)
    value -= 1

print("전체 실행 종료")

lst = ["ans", 100, 3.14]
for item in lst:
    print(item, type(item))

print(len(lst))

lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))
print("---continue")
for i in lst:
    if i%2 == 0:
        continue
    print("Item:{0}".format(i))

#수열함수
print(list(range(10)))
print(list(range(1,11)))


#year
print(list(range(2000,2023)))

##list comprehension(list embedding) : 한줄로 필터링, 루프 가공까지 파이썬스럽다. 축약
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])

#필터함수
lst = [20, 25, 30]
iterL = filter(None, lst)
for i in iterL:
    print("Item:{0}".format(i))

print("--filtering")

#필터링 함수 정의

def getBiggerThan20(i):
    return i >20

iterL = filter(getBiggerThan20, lst)
for i in iterL:
    print("Item:{0}".format(i))

#람다함수사용
print("--lamda--")
iterL = filter(lambda x:x>20, lst)
for i in iterL:
    print("Item:{0}".format(i))







