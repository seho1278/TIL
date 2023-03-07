# 16002번 합성수 방정식

T = int(input())

for t in range(T):
    N = int(input())
    x = 0
    y = 0
    cnt = 0
    list_ = []
    while True:
        if x-y == N:
            print(f'#{t+1} {x} {y}')
            break
        else:
            list_.append(cnt)
            cnt += 1