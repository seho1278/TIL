# 10818번 최소, 최대
N = int(input())
M = list(map(int, input().split()))

print(min(M), max(M), sep=' ')


# 11720번 숫자의 합
N = int(input())
M = input()
M_list = [int(a) for a in str(M)]
print(sum(M_list))


# 2750번 수 정렬하기
# 오름차순 정렬
N = int(input())
num_list = []
for n in range(N):
    num = int(input())
    num_list.append(num)

num_list = sorted(num_list)

for m in num_list:
    print(m)


# 2562번 최댓값
# 9개의 서로 다른 자연수 주어졌을때의 최댓값 구하기
num_list = []
cnt = 1
for n in range(9):
    num = int(input())
    num_list.append(num)

for m in num_list:
    if m == max(num_list):
        print(max(num_list), cnt, sep='\n')
    else:
        cnt += 1