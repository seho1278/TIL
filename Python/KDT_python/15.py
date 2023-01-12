# num = 2
# result = '홀' if num % 2 == 0 else '짝'
# print(result)



# r_list = []

# for t in range(1, 4):
#     r_list.append(t**3)
# print(r_list)

# print([n**3 for n in range(1, 4)])
# print({number : number**3 for number in range(1, 4)})

# numbers = ['1', '2', '3']
# new_numbers = list(map(int, numbers))



# numbers = [[2, 1], [1, 3]]
# new_numbers = list(map(sorted, numbers))
# print(new_numbers)


# def div_2(n):
#     return n//2

numbers = [2, 4]
# new_numbers = list(map(div_2, numbers))
new_numbers = list(map(lambda n: n//2, numbers))
print(new_numbers)


