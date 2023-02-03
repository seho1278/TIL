# 11286번 절댓값 힙

# 배열에 정수x (x != 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

# 입력 : 첫째 줄에 연산의 개수N이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 넣는 연산이고
# x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다.

# 출력 : 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for n in range(N):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

    else:
        heapq.heappush(heap, (abs(x), x))