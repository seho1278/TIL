# 11721번 열 개씩 끊어 출력하기
S = input()
a = 0
b = 10
while True:
    print(S[a:b]) 
    a += 10
    b += 10
    if S[a:b] == '':
        break