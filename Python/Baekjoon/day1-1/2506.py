# 2506번 점수계산
N = int(input())
marking = list(map(int, input().split()))
r_list = []
result = 0
for n in marking:
    if n == 1:
        result +=1
        r_list.append(result)
    else:
        result = 0
        r_list.append(result)

print(sum(r_list))