# 행 열 맞바꾸기

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]

traansposed_matrix = [[0]*3 for _ in range(4)]

for i in range(4):
    for j in range(3):
        traansposed_matrix[i][j] = matrix[j][i]


# 문제 적용

# 문제에서 이차원 리스트를 왼쪽, 오른쪽으로 90도 회전하는 경우
