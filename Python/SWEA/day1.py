# 2029 몫과 나머지 출력하기
# T = int(input())
# for t in range(T):
#     a, b = map(int, input().split())
#     print(f'#{t + 1} {a // b} {a % b}')


# 2071 평균값 구하기
# 첫줄에 테스트 케이스 T
# 각 테스트 케이스 첫 번째 줄에는 10개의 수가 주어진다.
# 출력의 각 줄은 #t로 시작하고 공백을 한칸 둔 다음 정답을 출력.

# T = int(input())
# result = 0       # 평균값을 담을 상자

# for t in range(1, T+1):
#     nums = list(map(int, input().split()))   # 입력값을 리스트로 받는다
#     result = round(sum(nums) / len(nums))    # 리스트로 받은 입력값들의 합을 갯수로 나눈뒤 반올림을 한 결과값을 result에 담는다
#     print(f'#{t} {result}')


# 1938 아주 간단히 계산기
# 1. 두개의 자연수 a, b는 1부터 9까지의 자연수이다.
# 2. 사칙연산 +, -, *, / 순서로 연산한 결과를 출력
# 3. 나누기 연산의 결과에서 소수점 이하의 숫자는 버린다.
# 입력으로 두개의 자연수 a, b 가 빈칸을 두고 주어진다
# 사칙연산의 결과를 각 줄에 순서대로 출력한다.
# import math        # 내장함수중엔 소수점 이하를 버리는 기능이 없어서 math 모듈을 불러온다.
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(math.trunc(a/b))


# 2046 스탬프 찍기
# 주어진 숫자 만큼 #을 출력
# T = int(input())
# print('#' * T)


# 2068 최대수 구하기
# 가장 첫줄에 테스트 케이스 T 입력
# 각 테스트 케이스 첫 번째 줄에 10개의 수 입력
# 가장 큰값 출력
# T = int(input())

# for t in range(1, T + 1):
#     nums = list(map(int, input().split()))  
#     print(f'#{t} {max(nums)}')









# 1000번 A+B

# A, B = map(int, input().split())
# print(A + B)

# # 2558번 A+B -2

# A = int(input())
# B = int(input())
# print(A + B)

# # 10950번 A+B -3
T = int(input())
result = 0

for t in range(T):
    A, B = map(int, input().split())
    result = A + B
    print(result)
