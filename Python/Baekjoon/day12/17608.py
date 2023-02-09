# 17608번 막대기
import sys

N = int(sys.stdin.readline())

list_ = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 1
last_stick = list_.pop()

for i in range(N-1):
    stick = list_.pop()
    if stick > last_stick:
        cnt += 1
        last_stick = stick

print(cnt)