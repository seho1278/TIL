# 10809번 알파벳 찾기
S = input()
alphabet = []

for n in range(97, 123):
    alphabet.append(chr(n))

r_list = []

for m in alphabet:
    result = 0
    if m in S:
        for l in S:
            if l == m:
                r_list.append(result)
                break
            else:
                result += 1
    else:
        r_list.append(-1)

print(*r_list)