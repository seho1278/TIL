# 9498번 시험 성적
N = int(input())

if N >= 90:
    print('A')

elif N >= 80 and 90 > N:
    print('B')

elif N >= 70 and 80 > N:
    print('C')

elif N >= 60 and 70 > N:
    print('D')

else:
    print('F')


# 9093번 단어 뒤집기
T = int(input())
for t in range(T):
    S = input().split()
    for s in S:
        print(s[::-1], end=' ')


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


# 2947번 나무 조각
numbers = list(map(int, input().split()))
r_numbers = sorted(numbers)

while True:
    if numbers != r_numbers:
        for n in range(len(numbers)-1):
            if numbers[n] > numbers[n+1]:      
                numbers[n], numbers[n+1] = numbers[n+1], numbers[n]
                print(*numbers)
    
    else:
        break
