# 4673번 셀프 넘버
# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의할 경우
# ex) d(75) = 75 + 7 + 5 = 87
# 양의정수 n이 주어졌을때, 이 수를 시작해서 n, d(n), d(d(n))... 과 같은 무한 수열을 만들 수 있다.
# ex) n = 33 : 33 + 3 + 3 > 39 + 3 + 9 > 51 + 5 + 1  ...
# n을 d(n)의 생성자라고 한다. ex) 33은 39의 생성자
# 생성자가 한개보다 많은 경우도 있다. ex) 91 + 9 + 1 = 101
# 이 때 생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프넘버는 총 13개가 있다. 1 3 5 7 9 20 31 42 ... 97
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오

# 입력 x

# 출력 : 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

# def d(x):
#     x_l = [int(a) for a in str(x)]
#     return x + sum(x_l)

# r_list = []
# for n in range(1, 10001):
#     r_list.append(d(n))

# for m in range(1, 10001):
#     if m not in r_list:
#         print(m)


# 1065번 한수
# 한수 : 어떤 양의 정수 X의 각 자리가 등차수열을 이루는 경우
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램 작성

# 입력 : 첫째 줄에 1000보다 작거나 같은 자연수 N 입력

# 출력 : 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수 출력

# def d(x):
#     x_l = [int(a) for a in str(x)]
#     return x_l

# N = int(input())
# result = 0
# for n in range(1, N+1):
#     if n < 10:
#         result += 1
#     elif 10 <= n and n < 100:
#         result += 1
#     elif 100 <= n and n < 1000:
#         if d(n)[2] - d(n)[1] == d(n)[1] - d(n)[0]:
#             result += 1

# print(result)

# 1065 -1 (함수없이)
# N = int(input())
# result = 0
# for n in range(1, N+1):
#     if n < 10:
#         result += 1
#     elif 10 <= n and n < 100:
#         result += 1
#     elif 100 <= n and n < 1000:
#         n_list = [int(a) for a in str(n)]
#         if n_list[2] - n_list[1] == n_list[1] - n_list[0]:
#             result += 1

# print(result)


# 1316번 그룹 단어 체커
# 그룸 단어란 각 문자가 연속해서 나타나는 경우만을 말한다.

# 입력: 첫줄에 단어의 개수N

# 출력: 그룹단어 갯수 출력

N = int(input())
result = 0

for n in range(N):
    S = input()
    cnt = 0
    index = S[0]        
    s_list = []

    if len(S) == 1:
        cnt = 1
    else:
        for i in S:     
            if i != index:
                s_list.append(index)
                index = i
        s_list.append(index)

        for m in s_list:
            if s_list.count(m) >= 2:
                cnt = 0
                break
            else:
                cnt = 1
                
        result += cnt

print(result) 