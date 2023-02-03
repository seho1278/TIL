# 11021번 A+B -7
T = int(input())

for t in range(1, T+1):
    A, B = map(int, input().split())
    print(f'Case #{t}: {A + B}')