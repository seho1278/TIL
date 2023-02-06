# 4963번 섬의 개수
import sys
sys.setrecursionlimit(10**6)  # DFS 깊이 범위를 정해준다. 런타임 에러 방지

def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:  # 범위 밖으로 나가게 되면 종료
        return False
    if graph[x][y] == 1:      # 노드가 방문하지 않은경우 
        graph[x][y] = 0       # 해당 노드 방문 처리
        dfs(x - 1, y)         # 재귀함수를 통해 인접 노드 탐색
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y + 1)
        dfs(x - 1, y - 1)
        dfs(x + 1, y - 1)
        dfs(x - 1, y + 1)
        return True
    return False

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))          # 2차원 리스트로 정보 입력

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                result += 1
    
    print(result)