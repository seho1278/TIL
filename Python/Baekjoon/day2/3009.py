# 3009번 네 번째 점
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해 필요한 네번째 점을 찾아라
# 입력 : 세 점의 좌표을 한줄에 하나씩 입력 1 <= (좌표) <= 1000
# 출력 : 네 번째 점의 좌표 출력
x = 0
y = 0
x_list = []
y_list = []

for n in range(3):
    numbers = list(map(int, input().split()))
    x_list.append(numbers[0])
    y_list.append(numbers[1])

for m in x_list:
    if x_list.count(m) == 1:
        x = m
        break

for l in y_list:
    if y_list.count(l) == 1:
        y = l
        break

print(x, y, sep=' ')