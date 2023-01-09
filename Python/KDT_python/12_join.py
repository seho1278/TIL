result = ['1', '5', '3']

# 153 출력?
# (1) print의 키워드(end)를 써서 출력
# (2) 반복하면서 문자열을 만든다

text = ''
for elem in result:
    text = text + elem
print(text)

# (2-2) join

print(''.join(result))


# 1 5 3
print(' '.join(result))