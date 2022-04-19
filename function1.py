# function1.py
# 함수 정의
def setValue(newValue):
    x = newValue
    print("함수내부 :", x)

#호출
#디버깅할때 중단점(break point)
retValue = setValue(5)
print(retValue)

#호출
#디버깅할 때 중단점(Break Point)
retValue = setValue(5)
print(retValue)

#교집합 문자를 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수
    result = []
    
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
print(intersect("HAM","SPAM"))

#정의되지않은 인자처리(**딕셔너리)

def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port +"/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

print(userURIBuilder("credu.com", "80", id = "kim", passwd="1234"))
print(userURIBuilder("credu.com", "80", id = "kim", passwd="1234", name="mike"))


#람다함수(이름이 없는 간결한 함수 정의): 일회용
#xy를 입력받고 xy곱해서 리턴
g= lambda x,y:x*y
print(g(3,4))
print(g(5,6))
#보통은 정의하고 바로 호출
print((lambda x:x*x)(3))
print(globals())









