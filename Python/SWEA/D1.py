# 2050 알파벳을 숫자로 변환
# S = input()

# for s in S:
#     print(ord(s) - 64, end=' ')


# 2043 서랍의 비밀번호
# P, K = map(int, input().split())

# print((P-K)+1)


# 1545 거꾸로 출력해 보아요
# N = int(input())

# for n in range(N, -1, -1):
#     print(n, end=' ')

T = int(input())

for t in range(T):
    numbers = map(int, input().split())
    result = 0
    for i in numbers:
        if i % 2 == 1:
            result += i
    print(f'#{t+1} {result}')