# 문제1
# n = input('문자열을 입력하세요 > ')

# result = 0
# for i in n:
#     if i == 'e':
#         result += 1

# print(result)


# 문제2 << 리스트 사용
# n = input('문자열을 입력하세요 > ')
# # dict_variable = {'a':'A', 'e':'E', 'i':'I', 'o':'O', 'u':'U'} 
# l = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
# result = 0

# for i in n:
#     if i in l:
#         result += 1

# print(result) 



# 문제3
# dict_variable = {
#     "이름": "정우영",
#     "생년월일": "20000101",
#     "회사": "하이퍼그로스",
# }

# dict_variable["나이"] = "24세"

# if "나이" not in dict_variable:
#     dict_variable["나이"] = "24세"

# print("나이 :", dict_variable["나이"])


# 문제4
# name = input("이름을 입력하세요 > ")
# phone = input("전화번호를 입력하세요 > ")
# address = input("거주지를 입력하세요 > ")

# dict_variable = {
#     "이름" : name,
#     "전화번호" : phone,
#     "거주지" : address
# }

# print(dict_variable)

# for keys, values in dict_variable.items():
#     print(keys, values, sep=' : ')


# 문제5
# name = input("이름을 입력하세요 > ")
# phone = input("전화번호를 입력하세요 > ")
# email = input("이메일을 입력하세요 > ")
# address = input("거주지를 입력하세요 > ")

# dict_variable = {
#     name : {
#     "전화번호" : phone,
#     "이메일" : email,
#     "거주지" : address}
# }

# print(dict_variable)


# 문제6
n = input('문자열을 입력하세요 > ')
dict_variable = {}

for i in n:
    if i not in dict_variable:
        dict_variable[i] = 1
    elif i in dict_variable:
        dict_variable[i] += 1

for keys, values in dict_variable.items():
    print(keys, values)
