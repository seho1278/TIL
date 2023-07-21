# heapq

### heapq
- list를 우선순위 큐처럼 사용할 수 있는 모듈이다.
- 기본은 0번 인덱스 값이 항상 최소값으로 저장되는 최소 힙이고, 우선순위 규칙을 정해줄 수 있다.

<br>

### Code
```python
import heapq

heap = list()

# heap list에 원소 추가
heapq.heappush(heap, 1)

# heap list에 원소 제거
heapq.heappop(heap, 1)

# heapq로 변환
heapq.heapify(heap)

# Max Heap 만들기
heap = list()
nums = [6, 2, 1, 4, 5, 3]
for num in nums:
  heapq.heappush(heap, (-num, num))
```