# ss = "Happy Birthday Happy"
# print(ss.count("Happy"))
# print(ss.split())
# print(ss.replace("Happy", "Hope", 2))

ss = "Happy"
# print("출력 문자열 ==> ", ss)
print("출력 문자열 ==> ", end = '')

if ss.startswith('(') == False :
    print("(", end = '')

print(ss, end = '')

if ss.endswith(')') == False :
    print(")", end= '')