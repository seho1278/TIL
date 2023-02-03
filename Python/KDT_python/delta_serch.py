# (1, 1)
# 위와 같은 조합이 들어왔을 때 상하좌우를 모두 출력하는 코드!

x = 1
y = 1
print(x, y)

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for dx, dy in delta:
    print(x + dx, y + dy)


for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    # 범위를 벗어나지 않으면 갱신
    if 0 <= nx < 3 and 0 <= ny < 3:
        x = nx
        y = ny