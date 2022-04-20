# try1.py

#함수 정의
def divied(a,b):
    return a/b
try:
    result = divied(5,0)
    
except TypeError:
    print("숫자여야 합니다")
except ZeroDivisionError:
    print("숫자여야 합니다")
except:
    print("예상하지 못한 에러")
else:
    print("결과:{0".format(result))
finally:
    print("한번 더 체크(무조건실행)")



print("전체 코드 실행 종료")


