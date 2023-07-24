# defaultdict

- 딕셔너리와 동일한 구조로 만드는 서브 클래스
- 작동하는 방식은 딕셔너리와 동일하지만 초기 자료형을 설정해줄 수 있어서 그래프의 연결관계를 만들어 줄 때 사용한다.
- 주로 키의 개수를 세거나, 리스트, 집합을 정리할 때 많이 사용한다.
- defaultdick의 장점은 key 값이 없어도 value를 넣을 수 있다.
- 초기값은 int로 설정되어 있음

```python
from collections import defaultdict

dic = defaultdict()

# 자료형을 리스트로 고정
dic = defaultdict(list)

# 양방향 그래프 선언
s, e = 1, 2
dic[1].append(2)
dic[2].append(1)

# 모든 원소 확인
dic.items()

# 모든 키 확인
dic.keys()
```