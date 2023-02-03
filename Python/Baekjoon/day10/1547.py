# 1547번 공

M = int(input())

cup = [1, 0, 0]
for m in range(M):
    X, Y = map(int, input().split())
    if cup[X-1] == 1 or cup[Y-1] == 1:
        cup[X-1], cup[Y-1] = cup[Y-1], cup[X-1]

if 1 in cup:
    print(cup.index(1)+1)
else:
    print(-1)