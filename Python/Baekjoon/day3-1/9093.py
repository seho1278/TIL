# 9093번 단어 뒤집기
T = int(input())
for t in range(T):
    S = input().split()
    for s in S:
        print(s[::-1], end=' ')