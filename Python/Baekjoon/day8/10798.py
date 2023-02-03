# 10798번 세로읽기
# 리스트를처음부터 만들생각하지 말고 통에 옮겨담을 생각 먼저!

list_ = [[0] * 15 for _ in range(5)]

for _ in range(5):
    S = list(input())
    N = len(S)
    for n in range(N):
        list_[_][n] = S[n]

for i in range(15):
    for j in range(5):
        if list_[j][i] == 0:
            pass

        else:
            print(list_[j][i], end='')