# 3052번 나머지
# 두 자연수 A, B가 있을 때, A%B는 A를 B로 나눈 나머지이다
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다음 서로 다른 값이 몇개 있는지를 출력하라

remainder = {}
for n in range(10):
    number = int(input())
    result = number % 42
    if result not in remainder:
        remainder[result] = 1
    else:
        remainder[result] += 1

print(len(remainder.keys()))