# 10871번 X보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []
for n in A:
    if n < X:
        result.append(n)

print(*result)