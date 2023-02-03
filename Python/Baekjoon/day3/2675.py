# 2675번 문자열 반복
# 문자열 S를 받을때 P번 반복해서 새 문자열 P를 만든후 출력

T = int(input())

for t in range(T):
    N, S = input().split()
    S_list = []
    for i in S:
        S_list.append(i*int(N))
    print(*S_list, sep='')