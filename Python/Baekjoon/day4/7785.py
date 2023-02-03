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