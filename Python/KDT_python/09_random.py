# 1. 모듈을 가져오는 것!
# import random
# print(random.sample(population, 45))

# numbers = range(1, 46)
# lucky_number = random.sample(numbers, 6)
# print(sorted(lucky_number))

# for i in range(5):
#     numbers = range(1, 46)
#     lucky_number = random.sample(numbers, 6)
#     print(sorted(lucky_number))

# .sort() : 메서드
#return : None
# 해당 리스트 자체를 정렬!
# number = [10, 2, 5]
# result = number.sort()
# print(result) # None
# print(numbers)

# sorted() : 함수
# return : 정렬된 리스트
# numbers = [10, 2, 5]

# students = ['a', 'b', 'c', 'd']
# random.shuffle(students)
# print(students)

# import datetime

# print(datetime.datetime.now())
# print(datetime.date(2023, 1, 5))
# today = datetime.date(2023, 1, 5)
# print(today)
# print(type(today))
# print(today.year)
# print(today.day)

# end = datetime.date(2023, 6, 14)
# print(end - today)

import os
print(os.listdir())