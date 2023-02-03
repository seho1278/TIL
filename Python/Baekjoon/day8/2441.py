# 2441번 별찍기 - 4

N = int(input())

for n in range(N):
    print((' ' * n) + ('*' * (N-n)))