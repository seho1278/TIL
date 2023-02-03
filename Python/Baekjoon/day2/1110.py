# 1110번 더하기 사이클
# ex) N = 26 -> 2 + 6 = 8 -> 68 -> 6 + 8 = 14 -> 84
# 입력 : 첫쨰 줄 N (0 <= N <= 99)
# 출력 : N의 사이클 길이 출력

def f(x):                              # 두자리의 수를 나눠서 합한 값을 리턴
    x_list = [int(a) for a in str(x)]  
    return sum(x_list)

def d(x):                              # 수의 오른쪽 값을 리턴
    x_list = [int(a) for a in str(x)]
    return x_list[-1]

def str_add(x, y):                     # 각 자리의 수를 문자열로 합한 뒤 정수값으로 리턴
    return int(str(x) + str(y))

N = int(input())
T = N                                  # 비교해야하는 입력값을 보존하기 위해 변숫값 T에 할당
result = 0                             # 식의 결과값
cnt = 0                                # 사이클 수
while True:                            # 무한반복
    cnt += 1
    result = str_add((d(T)), d(f(T)))
    if result == N:
        print(cnt)
        break
    else:
        T = result

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
    
    

    first = N[-1]
    second = N[0]

    sum_number = int(first) + int(second)

    new_number = N[-1] + str(sum_number[-1])

    cnt += 1

    if new_number == T:
        break

    N = new_number

print (cnt)