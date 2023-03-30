# 1026번 보물
# 길이가 N인 배열 A, B
# 함수 S = A[0] * B[0] + ... + A[N-1] * B(N-1)
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열, B는 재배열 하면 안된다.
# S의 최솟값을 출력하는 프로그램 작성


# 입력 : 첫째 줄에 N, 둘째 줄에 A 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다.
# 출력 : 첫째 줄에 S의 최솟값 출력

# N = int(input())
# A = [i for i in map(int, input().split())]
# B = [j for j in map(int, input().split())]

# result = 0
# for i in range(N):
#     result += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))

# print(result)


# 1049번 기타줄
# 기타에서 N개의 줄이 끊어졌을때, 되도록 돈을 적게쓰고 기타 줄을 교체하는 경우를 구하기

# 입력 : 첫 줄에 끊어진 기타 줄 수 N, 기타줄 브랜드 M개 둘재 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다.
# 출력 : 첫째 줄에 기타줄을 적어도 N개 사기 위해 필요한 돈의 최솟값 출력

# N, M = map(int, input().split())

# minpackage = 1001
# minpiece = 1001

# for i in range(M):
#     x, y = map(int, input().split())
#     minpackage = min(minpackage, x)
#     minpiece = min(minpiece, y)

# result = 0

# if minpackage > minpiece*6:
#     result += N * minpiece
# else:
#     result += (N//6) * minpackage

#     if (N%6)*minpiece > minpackage:
#         result += minpackage
#     else:
#         result += (N%6)*minpiece

# print(result)


#1246번 온라인 판매

# N, M = map(int, input().split())

# list_ = []
# result = 0

# for i in range(M):
#     A = int(input())
#     list_.append(A)

# list_ = sorted(list_)

# result2 = 0

# for i in range(M):
#     x = min(M - i, N)
    
#     if result < list_[i]*x:
#         result = list_[i]*x
#         result2 = list_[i]

# print(result2, result)


# 1343번 폴리오미노

# S = input()
# S = S.replace('XXXX', 'AAAA')
# S = S.replace('XX', 'BB')

# if 'X' in S:
#     print(-1)

# else:
#     print(S)


# 1417번 국회의원 선거(다시 풀어보기)
import heapq
N = int(input())
win = int(input())
nums = []

for i in range(N-1):
    num = int(input())
    heapq.heappush(nums, (-num, num))

cnt = 0
while nums:
    num = heapq.heappop(nums)[1]
    if num >= win:
        num -= 1
        win += 1
        cnt += 1
        heapq.heappush(nums, (-num, num))

print(cnt)

