# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# 2 5
# 4 6

# 인접 행렬 : 7 * 7
# 정점간의 관계를 표현하고 있는 행렬
# 정점의 개수인 N에 의해 크기가 정해진다.

N = 7
M = 7 # input 수 이면서 간선의 갯수
graph = [[0] * N for _ in range(N)]

# input
# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# 2 5
# 4 6

# # 0 1 
# graph[0][1] = 1
# graph[1][0] = 1

# # 0 2
# graph[2][0] = 1
# graph[0][2] = 1

# # 1 3
# graph[1][3] = 1
# graph[3][1] = 1

# for문으로 작성

for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1
