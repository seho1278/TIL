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