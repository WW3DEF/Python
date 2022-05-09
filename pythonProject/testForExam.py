# a=100
# b=50
# result = a+b
# print(result)
# print(a,'+',b,'=',result)
# print(f'{a} + {b} = {result}')
#
# c = int(input("c의 값 입력 : "))
# d = int(input("d의 값 입력 : "))
# print(f'{c} + {d} = {c+d}')

# def add(a,b) :
#     c = a + b
#     return c
#
# def minus(a,b) :
#     c = a - b
#     return c
#
# def multiply(a,b) :
#     c = a * b
#     return c
#
# def divide(a,b) :
#     c = float(a) / float(b)
#     return c
#
# sum = add(10, 20)
# print(f'총합은 {sum}')
# sum = minus(20, 10)
# print(f'총합은 {sum}')
# sum = multiply(10,30)
# print(f'총합은 {sum}')
# sum = divide(10,3)
# print(f'총합은 {sum}')
#
# abc = '반갑다 ' + \
#     '김종현 교수님은 ' + \
#     '파이썬 빌런이다'
# print(abc)

# print("{2:d} {1:05d} {0:5d}".format(100,200,300))
# print("{a},{b},{c}".format(a=100,b=200,c=300))
#
# print("I love {} and {}".format('sigong','zoa'))
# print('my favorite is {0} and {1}'.format('Python', 'Java'))
# print('my favorite is {a} and {b}'.format(b='Python', a='Java'))
#
# a= """파이썬
# 개싫음"""
# print(a)
# a = 'a'
# print('a is {}'.format(a))
#
# x, y, z = 1, 2, 3
# print('a is {0}, {1}, {2}'.format(x,y,z))
# print('a is {2}, {1}, {0}'.format(x,y,z))
#
# name = 'Steve'
# family = 'Jobs'
# print("""My name is {0} {1} """
#       """I am {1} {0}""".format(name,family))

# a=int(input("첫 번째 숫자를 입력하세요 : "))
# b=int(input("두 번째 숫자를 입력하세요 : "))
# c=int(input("더할 숫자를 입력하세요 : "))
# sum = 0
# for i in range(a,b+1,c) :
#     sum += i
#
# print(sum)

# for x in range(2,9,2):
#     for y in range(1,10):
#         print('{0} * {1} = {2}'.format(x,y,x*y))
#     print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# import random
#
# tries = 0
# guess = 0
# answer = random.randint(1, 100)
#
# print('1부터 100 사이의 숫자를 맞추시오')
#
# while guess != answer :
#     guess = int(input('숫자를 입력하시오 : '))
#     tries += 1
#     if guess < answer :
#         print('너무 낮음')
#     else :
#         print('너무 높음')
# if guess == answer :
#     print('총 시도횟수 {0}번 정답은 {1}'.format(tries,answer))
#
# print(1,2,3,4, end='')

# i, k = 0, 0
#
# i = 0
# while i < 9:
#     if i < 5:
#         k = 0
#         while k < 4 - i:
#             print(' ', end='')
#             k+= 1
#         k = 0
#         while k < i * 2 + 1 :
#             print('\u2605', end='')
#             k += 1
#     else :
#         k = 0
#         while k < i - 4:
#             print(' ', end='')
#             k += 1
#         k = 0
#         while k < (9-i) * 2 - 1:
#             print('\u2605', end='')
#             k+=1
#     print()
#     i += 1

# aa = [0,0,0,0]
# sum = 0
#
# for i in range(0,4):
#     aa[i] = int(input("{0}번째 숫자를 입력하세요 : ".format(i)))
#     print('{0}번째 숫자의 값은 = {1}'.format(i,aa[i]))
#     sum += aa[i]
# print(f'총 합계는 {sum}')

# arr = [10,20,30,30,40,50]
# arrb = [60,70,80,90,100]
# print('{0} and {1}'.format(arr[-1],arr[-5]))

# print(arr[0:5] + \
# arr[2:5] + \
# del(arr[1])
# print(arr[::])
# arr.append(20)
# print(arr[::])
# print(len(arr))
# print(arr.count(30))
# arr.remove(30)
# arr.extend(arrb)
# print(sorted(arr[::]))

# tt3 = (10,20,30); tt3
# del(tt3)
# print(tt3)
data = {"철수":98,"영희":80,"순이":100,"돌이":70}

for i in data.keys():
    print("%s %d" % (i,data[i]))
    sum = data.values()
    avg = sum / i
print('==============')
print(avg)