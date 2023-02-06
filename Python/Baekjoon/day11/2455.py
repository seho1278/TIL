# 2455번 지능형 기차

result = 0
max_result = 0

for _ in range(4):
    A, B = map(int, input().split())
    result -= A
    result += B
    if max_result < result:
        max_result = result

print(max_result)