my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
# my_list2 = []

# for i in my_list:
#     if i not in my_list2:
#         my_list2.append(i)

# result = 0
# for i in my_list2:
#     result +=1

# print(my_list2)
# print(result)

# my_list2 = set(my_list)
# print(len(my_list2))


my_dict = {}

for i in my_list:
    if i not in my_dict:
        my_dict[i] = my_list.count(i)
print(my_dict)