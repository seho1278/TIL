# permutations

### permutations(iterable, r)
- python의 경우 내장 라이브러리인 permutaions()를 사용하면 순열을 직접 구현할 필요없이 순열을 만들어준다.
- permutations(iterable, r)는 두개의 인자 iterable과 r을 필요로 하는데, iterable에는 순열을 뽑을 반복 가능할 개체(list, string 등), r에는 뽑고자 하는 순열의 길이를 넣으면 된다.
- permutations()함수는 해당 길이의 가능한 모든 순열을 순서대로 반환한다.

### Code
```python
from itertools import permutations

A = [1, 2, 3, 4]
for P in permutaions(A, 2):
  print(P)

# OUTPUT
# (4, 1)
# (4, 3)
# (4, 2)
# (1, 4)
# ...
# (2, 3)

```