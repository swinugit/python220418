# db1.py

import sqlite3

#연결객체를 만들기
#파일에 데이터베이스를 저장
con = sqlite3.connect("/Users/seo/Desktop/work/commit.db")
#구문을 수행할 커서 객체
cur = con.cursor()
#테이블 구조(테이블 스키마):SQL구문읜 대소문자 구분안함
cur.execute("create table phonebook (name text, phonenum text);")
#1건을 입력
cur.execute("insert into phonebook values ('derick', '010');")
#입력 파라메터 처리
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into phonebook values (?, ?);", (name, phoneNumber))
#n건을 입력(2 차원 행렬 2행2열)
datalist = (("tom","010-123"), ("dsp","010-333"))
cur.executemany("insert into phonebook values (?, ?);", datalist)


#검색
cur.execute("select * from phonebook;")
#for row in cur:
#    print(row)

print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
cur.execute("select * from phonebook;")
print(cur.fetchall())