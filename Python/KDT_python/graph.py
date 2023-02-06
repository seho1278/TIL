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

# N = 7
# M = 7 # input 수 이면서 간선의 갯수
# graph = [[0] * N for _ in range(N)]

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

# for i in range(M):
#     n1, n2 = map(int, input().split())
#     graph[n1][n2] = 1
#     graph[n2][n1] = 1



# DFS
graph = [
    [1, 2],
    [0, 3, 4],
    [0, 4, 5],
    [1],
    [1, 2, 6],
    [2],
    [4]
]


visited = [False] * n # 방문 처리 리스트 만들기

start = 0 # 시작 노드

stack = [start] # 돌아갈 곳을 기록
visited[start] = True

# 방문 시작
while stack: # 스택이 빌 때 까지
    cur = stack.pop()

    for adj in graph[cur]:
        if not visited[adj]:
            visited[adj] = True
            stack.append(adj)

# 1. 0
# stack : [0]
# visited : [True, False, False, False, False, False, False]
'''
cur = stack.pop()
# current : 0

for adj in [1, 2]: # 0과 인접한 노드
    # 첫번째 시행 때 adj : 1
    if not visited[1]: # 방문을 안했으면 False니까 not으로 뒤집음
        visited[adj] = True # 방문 체크
        stack.append(adj) # 기록

    if not visited[2]: # 방문을 안했으면 False니까 not으로 뒤집음
        visited[adj] = True # 방문 체크
        stack.append(adj) # 기록
'''

# stack 