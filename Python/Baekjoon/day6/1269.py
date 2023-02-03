# 1269번 대칭 차집합

# 자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다.
# 이 때 두 집합의 대칭 차집합의 원소의 개수를 출력

A, B = map(int, input().split())
A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

print(len((A_set | B_set) - (A_set & B_set)))