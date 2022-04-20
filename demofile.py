#demofile.py

url = "http://www.credu.com/?page=" + str(1)
print(url)

for x in range(1,6):
    print(x, "*", x, "=", x*x)

print("약간변경")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("약간변경")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(10))


print("{0:x}".format(10145335))
print("{0:b}".format(10))
print("{0:,}".format(150000))
print("{0:e}".format(14/3))
print("{0:f}".format(14/3))
print("{0:.2f}".format(14/3))



#파일을 생성하기
f = open("/Users/seo/Desktop/work/demo.txt", "wt", encoding="utf-8")
f.write("하나\n두번째\n세번째\n")
f.close()
