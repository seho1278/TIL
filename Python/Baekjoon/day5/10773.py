# 10773번 제로

K = int(input())
result = []
for k in range(K):
    number = int(input())
    if number == 0:
        result.pop()
    else:
        result.append(number)
print(sum(result))