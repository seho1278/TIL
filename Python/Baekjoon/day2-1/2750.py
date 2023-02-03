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