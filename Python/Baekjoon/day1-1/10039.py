# 10039번 평균 점수
N = int(input())

result = []
for n in range(N):
    N = int(input())
    if N >= 40:
        result.append(N)
    else:
        result.append(40)

print(round(sum(result)/len(result)))