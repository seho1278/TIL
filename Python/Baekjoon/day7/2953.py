# 2953번 나는 요리사다

rank = {}
for n in range(1, 6):
    score = map(int, input().split())
    rank[n] = sum(score)


print(*max(rank.items(), key=lambda x:x[1]))