# 7568번 덩치

N = int(input())

list_ = []
for n in range(N):
    M = list(map(int, input().split()))
    list_.append(M)

result = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if list_[i][0] < list_[j][0] and list_[i][1] < list_[j][1]:
            cnt += 1
    else:
        result.append(cnt)

print(*result, end=' ')

    