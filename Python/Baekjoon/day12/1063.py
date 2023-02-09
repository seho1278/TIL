# 1063번 킹

# 킹 이동
def move(x, y, z):
    if z == 'R':
        if y+1 <= 7:
            return chess[x][y+1]
        else:
            return chess[x][y]
    if z == 'L':
        if y-1 >= 0:
            return chess[x][y-1]
        else:
            return chess[x][y]
    if z == 'B':
        if x+1 <= 7:
            return chess[x+1][y]
        else:
            return chess[x][y]
    if z == 'T':
        if x-1 >= 0:
            return chess[x-1][y]
        else:
            return chess[x][y]
    if z == 'RT':
        if x-1 >= 0 and y+1 <= 7:
            return chess[x-1][y+1]
        else:
            return chess[x][y]
    if z == 'LT':
        if x-1 >= 0 and y-1 >= 0:
            return chess[x-1][y-1]
        else:
            return chess[x][y]
    if z == 'RB':
        if x+1 <= 7 and y+1 <=7:
            return chess[x+1][y+1]
        else:
            return chess[x][y]
    if z == 'LB':
        if x+1 <= 7 and y-1 >= 0:
            return chess[x+1][y-1]
        else:
            return chess[x][y]

# 킹 좌표
def l(x):
    for m in range(8):
        for k in range(8):
            if chess[m][k] == x:
                return m, k
    
# 체스판-------------------------------------
h = ['8', '7', '6', '5', '4', '3', '2', '1']
w = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

chess = [[0] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        chess[i][j] = w[j] + h[i]
        
# -------------------------------------------

A, B, N = input().split()
N = int(N)
stone = l(B) # 돌 좌표값
king = l(A)  # 킹 좌표값
for n in range(N):
    M = input()
    if move(*king, M) == chess[stone[0]][stone[1]]:
        if chess[stone[0]][stone[1]] != move(*stone, M):
            king = l(move(*king, M))
            stone = l(move(*stone, M))
    else:
        king = l(move(*king, M))

print(chess[king[0]][king[1]], chess[stone[0]][stone[1]], sep='\n')