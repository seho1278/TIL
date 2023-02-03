# 1652번 누울 자리를 찾아라

# N X N의 정사각형 모양의 콘도의 방 안에 연식이가 누울 자리 찾기
# 똑바로 연속해서 2칸 이상의 빈칸이 존재하면 누울 수 있다.
# 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하라

# 입력 : 첫째 줄 방에 크기 N이 주어진 뒤 N줄에 걸쳐 N개의 문자 입력, .는 아무것도 없는곳, X는 짐이 있는 곳을 의미

# 출력 : 첫째 줄에 가로로 누울 수 잇는 자리와 세로로 누울 수 있는 자리의 개수를 출력


# 오답코드 (..xx.. 일때 2개가 된다는걸 이해 못했다..)
# N = int(input())

# matrix = [list(input()) for _ in range(N)]

# row, col = 0, 0
# for i in range(N):    
#     for j in range(N-1):
#         if matrix[i][j] == '.' and matrix[i][j+1] == '.':
#             row += 1
#             break

# for i in range(N):
#     for j in range(N-1):
#         if matrix[j][i] == '.' and matrix[j+1][i] == '.':
#             col += 1
#             break

# print(row, col)


# 정답 코드
N = int(input())

matrix = [list(input()) for _ in range(N)]

row, col = 0, 0
for i in range(N):    
    cnt = 0
    for j in range(N):
        if matrix[i][j] == '.':
            cnt += 1
            
        else:
            if cnt >= 2:
                row += 1
            cnt = 0
    else:
        if cnt >= 2:
            row += 1


for i in range(N):    
    cnt2 = 0
    for j in range(N):
        if matrix[j][i] == '.':
            cnt2 += 1
    
        else:
            if cnt2 >= 2:
                col += 1
            cnt2 = 0

    else:
        if cnt2 >= 2:
            col += 1
            

print(row, col)