#demofile2.py

#파일을 생성하기
f = open("/Users/seo/Desktop/work/demo.txt", "wt", encoding="utf-8")
f.write("하나\n두번째\n세번째\n")
f.close()

#파일을 읽기
f = open("/Users/seo/Desktop/work/demo.txt", "rt", encoding="utf-8")
#전체 파일을 하나의 문자열 변수로 받기
result = f.read()
print(result)
#현재 파일 포인터의 위치(책갈피같은것)
print(f.tell())
#처음으로 리셋
f.seek(0)
#예를들면 파일이 1기가, 2기가(로그파일)
print(f.readline(), end="")
print(f.readline(), end="")

#파일 전체를 리스트로 받기
f.seek(0)
lst = f.readlines()
print(lst)

f.close()

#기존 파일에 첨부하는 경우
f = open("/Users/seo/Desktop/work/demo.txt", "a+", encoding="utf-8")
f.write("새로운 데이터\n")
f.close()

