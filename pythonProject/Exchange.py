A = 0;
A= int(input('교환할 돈은 얼마 '))

print(f'500원짜리 ==> {int(A/500)}개')
A %= 500
print(f'100원짜리 ==> {int(A/100)}개')
A %= 100
print(f'50원짜리 ==> {int(A/50)}개')
A %= 50
print(f'10원짜리 ==> {int(A/10)}개')
A %= 10
print(f'바꾸지 못한 잔돈 ==> {A}원')