print("%d %d" % (100, 200))

print("%d and %d" % (100, 200))

print("a=%d b=%d" % (100, 200))
a=100
b=200

print("%d %f %d" % (100,200.00,300))

print(1,2)

# end - 마지막 출력 문자 지정(기본값 = \n)
print(1,2, end='/')
print(1,2,3,4,5)

# format - 위치인자를 이용한 출력
print("{} {} {}".format(10, 20, 30))
print("{0} {1} {2}".format(10, 20, 30))
print("{2} {1} {0}".format(10, 20, 30))
print("a={} b={} c={}".format(10, 20, 30))
print("{a} {b} {c}".format(a=10, b=20, c=30))

#서식 출력
print("%d %d %d"%(100, 200, 300))
print("x= %d y = %5d z=%05d" % (100, 200, 300))


#using format() method
print("I love {} for {}!".format('Python', 'Coding'))

# escape sequence
# \n 새로운 줄로 이동
# \t 다음 탭으로 이동
# \b 뒤로 한칸 이동
# \\ \출력
# \' '출력
# \" "출력

print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("글자가 \"강조\"되는 효과1")
print("글자가 \'강조\'되는 효과2")
print("\\\\\\ 역슬래시 세 개 출력")
print(r"\n \t \" \\를 그대로 출력")