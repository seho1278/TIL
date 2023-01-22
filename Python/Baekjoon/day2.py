# # 9085번 더하기
# # 10보다 작거나 같은 자연수 N개의 합 구하기
# # 입력 : 첫줄 테스트 케이스 개수 T, 각 테스트 케이스 첫줄 자연수 개수 N, 다음줄에 N개의 자연수 입력
# # 출력 : 각 테스트 케이스에서 주어진 자연수의 합을 출력

# T = int(input())

# for t in range(T):
#     N = int(input())
#     numbers = list(map(int, input().split()))
    
#     print(sum(numbers))


# # 10824번 네 수
# # 네 자연수 A, B, C, D 주어졌을 때, A, B를 붙인 수와 C, D를 붙인 수의 합을 구하라
# # ex A : 20, B : 30 = 2030
# # 입력 : 첫줄 네 자연수 A, B, C, D
# # 출력 : A, B / C, D 붙인 수의 합 출력

# A, B, C, D = input().split()
# print(int(A + B) + int(C + D))


# # 3009번 네 번째 점
# # 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해 필요한 네번째 점을 찾아라
# # 입력 : 세 점의 좌표을 한줄에 하나씩 입력 1 <= (좌표) <= 1000
# # 출력 : 네 번째 점의 좌표 출력
# x = 0
# y = 0
# x_list = []
# y_list = []

# for n in range(3):
#     numbers = list(map(int, input().split()))
#     x_list.append(numbers[0])
#     y_list.append(numbers[1])

# for m in x_list:
#     if x_list.count(m) == 1:
#         x = m
#         break

# for l in y_list:
#     if y_list.count(l) == 1:
#         y = l
#         break

# print(x, y, sep=' ')


# # 10952번 A+B -5

# while True:
#     A, B = map(int, input().split())

#     if A == 0 & B == 0:
#         break
#     else: 
#         print(A + B)


# # 1110번 더하기 사이클
# # ex) N = 26 -> 2 + 6 = 8 -> 68 -> 6 + 8 = 14 -> 84
# # 입력 : 첫쨰 줄 N (0 <= N <= 99)
# # 출력 : N의 사이클 길이 출력

# def f(x):                              # 두자리의 수를 나눠서 합한 값을 리턴
#     x_list = [int(a) for a in str(x)]  
#     return sum(x_list)

# def d(x):                              # 수의 오른쪽 값을 리턴
#     x_list = [int(a) for a in str(x)]
#     return x_list[-1]

# def str_add(x, y):                     # 각 자리의 수를 문자열로 합한 뒤 정수값으로 리턴
#     return int(str(x) + str(y))

# N = int(input())
# T = N                                  # 비교해야하는 입력값을 보존하기 위해 변숫값 T에 할당
# result = 0                             # 식의 결과값
# cnt = 0                                # 사이클 수
# while True:                            # 무한반복
#     cnt += 1
#     result = str_add((d(T)), d(f(T)))
#     if result == N:
#         print(cnt)
#         break
#     else:
#         T = result

# class addcycle:
#     def __init__(self, number):
#         self.number = number
  
#     def cycle(number):
#         def f(x):
#             x_list = [int(a) for a in str(x)]  
#             return sum(x_list)

#         def d(x):                             
#             x_list = [int(a) for a in str(x)]
#             return x_list[-1]

#         def str_add(x, y):                  
#             return int(str(x) + str(y))

#         T = number
#         result = 0                         
#         cnt = 0                               
#         while True:                           
#             cnt += 1
#             result = str_add((d(T)), d(f(T)))
#             if result == number:
#                 return cnt
#             else:
#                 T = result

# N = int(input())
# res = addcycle(N)
# print(res.cycle())

# N = "26"
# T = N
# cnt = 0

# if int(N) < 10:
#         N = "0" + N

# while True:
    
    

#     first = N[-1]
#     second = N[0]

#     sum_number = int(first) + int(second)

#     new_number = N[-1] + str(sum_number[-1])

#     cnt += 1

#     if new_number == T:
#         break

#     N = new_number

# print (cnt)