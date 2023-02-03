# 9085번 더하기
# 10보다 작거나 같은 자연수 N개의 합 구하기
# 입력 : 첫줄 테스트 케이스 개수 T, 각 테스트 케이스 첫줄 자연수 개수 N, 다음줄에 N개의 자연수 입력
# 출력 : 각 테스트 케이스에서 주어진 자연수의 합을 출력

T = int(input())

for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    print(sum(numbers))