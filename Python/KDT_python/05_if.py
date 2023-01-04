# 예제1
# if 5 > 3:
#     print('크다!')
# else:
#     print('작다!')
# print('!!!!!')


# 예제2
# a = -10
# if a >= 0:
#     print('양수')
# else:
#     print('음수')
# print(a)


# 실습 문제1
# num = int(input())

# if num <= 0:
#     print('양의 정수를 입력하세요')
# else:
#     if num % 2 == 0:
#         print('짝수')
#     else:
#         print('홀수')
#     print(num)


# 실습 문제2
# dust = int(input())
# if 0 <= dust <= 30:
#     print('좋음')
# elif 30 < dust <= 80:
#     print('보통')
# elif 80 < dust <= 150:
#     print('나쁨')
# else:
#     print('매우나쁨')

# dust = int(input())
# if dust > 150:
#     print('매우 나쁨')
# elif dust > 80:
#     print('나쁨')
# elif dust > 30:
#     print('보통')
# else:
#     print('좋음')
# print('미세먼지 확인 완료')

# a = range(4)
# print(list(a))

# a = 'apple'

# for char in a:
#     print(char)

# l = ['윤원', '용진', '필진']

# for name in l:
#     print(name)
#     # print(l[0])
#     # print(l[1])
#     # print(l[2])

# a = 'apple'

# # 1.
# # 반복 가능한 객체 : 각 요소가 필요할 때
# for char in a:
#     print(char)
# # 2.
# # 반복 가능한 객체 : 인덱스가 필요할 때
# for i in range(len(a)):
#     print(i, a[i])

word = 'apple'
# a가 있으면, 1을 출력
for char in word:
    # print(char)
    if char == 'a':
        print(1)
    