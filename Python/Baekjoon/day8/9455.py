# 9455번 박스
# m x n 행 박스가 움직인 거리는 바닥에 쌓익 전 까지 이동한 칸의 개수

# 입력 : 첫째 줄에 테스트 케이스 개수 T, 각 테스트 케이스 첫째 줄에 m과 n, 다음 그리드의 각 행의 정보를 나타내는 n개의 정수
# 박스가 들어있는 칸은 1로 다른 칸은 0으로 주어진다.

# 출력 : 각 테스트 케이스마다 입력으로 주어진 그리드에서 모든 박스가 이동한 거리를 출력

# T = int(input())

# for t in range(T):
#     m, n = map(int, input().split())
#     box = [list(map(int, input().split())) for _ in range(m)]
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if box[j][i] == 1:
#                 for k in range(j, m):
#                     if box[k][i] == 0:
#                         cnt += 1
#     print(cnt)


# 다른사람 코드

grid = [
    [0, 0],
    [0, 1],
    [1, 0],
    [0, 0],
    [0, 1],
]

m = 5 # 세로
n = 2 # 가로

for x in range(n):
    for y in reversed(range(m)):
        if grid[y][x] == 1:
            while True:
                if y+1 == m:
                    break

                if grid[y+1][x] == 1:
                    break                

                grid[y][x] = 0

                grid[y+1][x] = 1

                y += 1
                # 다음 탐색
