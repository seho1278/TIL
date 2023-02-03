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