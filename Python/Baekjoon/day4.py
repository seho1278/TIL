# 2576번 홀수
# 7개의 자연수가 주어질 때
# 홀수 자연수들 골라 합을 구하고 고른 홀수들 중 최솟값을 찾는 프로그램 작성

odd = []
for n in range(7):
    N = int(input())
    if N % 2 == 1:
        odd.append(N)

if len(odd) == 0:
    print(-1)

else:
    print(sum(odd), min(odd), sep='\n')


# 10822번 더하기
# 숫자와 콤마로만 이루어진 문자열 S에 포함되어 있는 자연수의 합 구하기
S = input()
print(sum(map(int, S.split(','))))


# 2754번 학점계산
N = input()
result = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
if N != 'F':
    if N[1] == '0':
        print(result[N[0]])
    elif N[1] == '+':
        print(result[N[0]] + 0.3)
    else:
        print(result[N[0]] - 0.3)

else:
    print(result[N[0]])


# 5622번 다이얼
# 숫자를 하나 누를 때 마다 다이얼이 처음위치로 돌아간다
# 숫자 1을 걸려면 총 2초 필요, 한칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다.
# 할머니가 외운 단어가 주어졌을 때 전화를 걸기 위해 필요한 최소 시간을 구하는 프로그램 작성

# 입력 : 첫줄 알파벳 대문자 단어가 주어진다.
# 출력 : 첫줄에 다이얼을 걸기 위해 필요한 최소시간 출력

S = input()
dial = {
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10
}
d_list = []
for s in S:
    for key, value in dial.items():
        if s in key:
            d_list.append(value)

print(sum(d_list))


# 2577번 숫자의 개수
# 3개의 자연수 A, B, C 가 주어질 때 A * B * C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇번씩 쓰였는지 구하는 프로그램 작성
# ex) A = 150, B = 266, C = 427 / A*B*C = 17037300 0이 3번....
# 입력 : 1줄A 2줄B 3줄C
# 출력 : 1부터 9까지 숫자가 몇번쓰엿는지 차례로 한줄에 하나씩 출력

A = int(input())
B = int(input())
C = int(input())
mul = A*B*C
result = {}

for i in range(10):
    result[i] = 0

for n in result.keys():
    for s in str(mul):
        if int(s) == n:
            result[n] += 1

print(*result.values(), sep='\n')


# 7785번 회사에 있는 사람
# 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램 작성

# 입력 : 첫째 줄에 로그에 기록된 출입 기록의 수 n 다음 n개의 줄에는 출입 기록이 순서대로 주어진다.
# 각 사람의 이름이 주어지고 enter:출근 이나 leave:퇴근 이 주어진다 (동명이인x)

# 출력 : 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한줄에 한명씩 작성

import sys
N = int(sys.stdin.readline())
company = {}

for n in range(N):
    name, log = input().split()
    if log == 'enter':
        company[name] = log
    else:
        del company[name]

company = sorted(company.keys(), reverse=True)

for i in company:
    print(i)