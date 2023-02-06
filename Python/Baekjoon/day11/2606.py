# 2606번 바이러스
# import sys

# N = int(sys.stdin.readline())
# M = int(sys.stdin.readline())

# graph = [[] for _ in range(N+1)]
# visited = [False] * (N + 1)
# for m in range(M):
#     v1, v2 = map(int, sys.stdin.readline().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)

# visited = [False] * N

# def dfs(start):
#     stack = [start]
#     visited[start] = True

#     while stack:
#         cur = stack.pop()

#         for adj in graph[cur]:
#             if not visited[adj]:
#                 visited[adj] = True
#                 stack.append(adj)

# dfs(1)
# print(visited.count(True))

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
for m in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

stack = [1]
visited[1] = True

while stack:
    cur = stack.pop()

    for adj in graph[cur]:
        if not visited[adj]:
            visited[adj] = True
            stack.append(adj)


print(visited.count(True)-1)

