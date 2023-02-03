# 1225번 이상한 곱셈
import sys

A, B = sys.stdin.readline().split()
sum_list = []
sum_list.append(list(map(int, A)))
sum_list.append(list(map(int, B)))


print(sum(sum_list[0]) * sum(sum_list[1]))