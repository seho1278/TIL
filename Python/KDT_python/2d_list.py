# 행 우선출력

# list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in list_:
#     for j in i:
#         print(j)

# 열 우선출력

# for i in range(len(list_)):
#     for j in list_:
#         print(j[i])

# 이차원리스트 총합

# result = 0
# for i in list_:
#     result += sum(i)
# print(result)

# print(sum(map(sum, list_)))


# 이차원리스트 최댓값:

# for i in list_:
#     max_result = max(i)
# print(max_result)


# 리스트 회전(shift 연산)
# list_ = [1, 2, 3, 4, 5]

# list_.insert(0, list_.pop())

# print(list_)
# ------------------------------------
# N= len(list_)
# new_list = [None for _ in range(N)]

# print(list_, new_list)

# for i in range(N):
#     new_list[i-1] = list_[i]
#     print(new_list)

# n = 2
# N= len(list_)
# new_list = [None for _ in range(N)]

# print(list_, new_list)

# for i in range(N):
#     print((i+n)%N)
#     new_list[(i+n)%N] = list_[i]
#     print(new_list)

# for n in range(5):
#     print(list_[-n:] + list_[:-n])

# from collections import deque
# d = deque(list_)
# d.rotate(2)
# print(d)



# list_ = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 8, 0, 1]
#     ]


