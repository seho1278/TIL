# 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정할 경우
# 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수를 구하라
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

# 내 코드
N = int(input())
result = 0
while True:    
    if N // 500 != 0:
        result += N // 500
        N = N % 500
    elif N // 100 != 0:
        result += N // 100
        N = N % 100
    elif N // 50 != 0:
        result += N // 50
        N = N % 50
    else:
        result += N // 10
        print(result)
        break

# 답안 예시
# 최적의 해를 빠르게 구하기 위해서는 가장 큰 화폐 단위부터 돈을 거슬러 준다.
# N원을 거슬러 줘야 할 때, 가장 먼저 500원으로 거슬러 줄 수 있을 만큼 거슬러준다.
# 이후 100원 50원 10원짜리 동전을 차례대로 거슬러 줄 수 있을 만큼 거슬러 준다.
N = 1260
count = 0

# 큰 단위부터 차례대로 확인
array = [500, 100, 50, 10]

for coin in array:
    count += N // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    N %= coin  # N을 coin으로 나눈 나머지

print(count)