# 2577번 숫자의 개수
# 3개의 자연수 A, B, C 가 주어질 때 A * B * C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇번씩 쓰였는지 구하는 프로그램 작성
# ex) A = 150, B = 266, C = 427 / A*B*C = 17037300 0이 3번....
# 입력 : 1줄A 2줄B 3줄C
# 출력 : 1부터 9까지 숫자가 몇번쓰엿는지 차례로 한줄에 하나씩 출력

A = int(input())
B = int(input())
C = int(input())
mul = A*B*C
result = {}

for i in range(10):
    result[i] = 0

for n in result.keys():
    for s in str(mul):
        if int(s) == n:
            result[n] += 1

print(*result.values(), sep='\n')