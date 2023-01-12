# 2439번 별 찍기 - 2
# N = int(input())

# for n in range(1, N + 1):
#     print(('*' * n).rjust(N))


# 10952번 A+B -5
# import sys          # input 대신 sys 모듈을 불러와 사용

# while True:         # 무한반복 설정
#     A, B = map(int, sys.stdin.readline().split())
#     if A == 0 and B == 0:
#         break       # 0, 0 조건을 만족하면 종료#23110T-update
      
#     else:           # 0, 0이 아닌경우 A + B 출력
#         print(A + B)


#10951번 A+B - 4
# while True:         # 무한반복 설정
#     try:
#         A, B = map(int, input().split())  # sys를 사용하면 EOFError를 raise하지 않기 때문에 input() 사용!
#         print(A+B)
#     except EOFError:    # 에러가 발생하면 종료되도록 설정
#         break


# 1110 더하기 사이클
# 0보다 크거나 같고, 99보다 작거나 같은 정수 N
# 먼저 주어진 수 < 10 : 앞에 0을 붙여 두자리 수로 만들고 각자리의 숫자를 더한다.
# 그다음 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어붙이면 새로운 수를 만들 수 있다.
# ex) 26부터 시작 2 + 6 = 8, 새로운 수는 68 6 + 8 = 14 새로운 수는 84이다 8 + 4 = 12 새로운 수는 42이다 4 + 2 = 6이다. 새로운 수는 26이다
# 위의 예는 4번만에 원래 수로 돌아올 수 잇따. 따라서 26의 사이클 길이는 4이다.
# N이 주어졌을 때, N의 사이클 길이를 구하는 프로그램 작성

# N = int(input())
# result = 0
# T = N
# r_list = []


# while True:
#     if T >= 10:
#         result = (T//10) + (T%10)
#         result = int(str(T%10) + str(result%10))
    
#     else:
#         result = 0 + T
#         result = int(str(T%10) + str(result%10))

#     if result != N:
#         r_list.append(result)
#         T = result

#     else:
#         r_list.append(result)
#         break

# print(len(r_list))

# 다른 풀이
# N = str(input()).zfill(2)
# result = 0
# T = N
# count = 0


# while True:
#     count += 1

#     result = T[1] + str(int(T[0]) + int(T[1])).zfill(2)[1]
#     result = str(result).zfill(2)
    
    
#     if int(result) == int(N):
#         break
#     else:
#         T = result

# print(count)




# 10807번 개수 세기
# N개 정수 주어졌을 때 정수 v가 몇개인가
# 첫 줄에는 정수 개수 N
# 둘째 줄에는 정수 공백
# 셋째 줄에는 찾으려는 정수 v가 주어진다

# N = int(input())
# numbers = list(map(int, input().split()))
# v = int(input())

# print(numbers.count(v))

# h, w = map(int, input().split())
# n = int(input())
# l, d, (x, y) = map(int, input().split())