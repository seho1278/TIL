# # 블랙잭

# N = 5
# M = 21

# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             pass

# range(5)돌리는거랑 시간복잡도가 똑같다
# 3중for문 들어가는순간 시간복잡도는n^3


# (1, 1)
# 위와 같은 조합이 들어왔을 때 상하좌우를 모두 출력하는 코드!

x = 1
y = 1
print(x, y)

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for dx, dy in delta:
    print(x + dx, y + dy)
