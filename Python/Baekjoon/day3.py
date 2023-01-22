# 10988번 팰린드롬인지 확인하기
# 앞으로 읽을때랑 거꾸로 읽을때랑 똑같은 단어인지 확인하기

S = input()

if S[:] == S[::-1]:
    print(1)
else:
    print(0)

# S = input()
# n = 0
# while True:
#     if S[n] == S[-n-1]:
#         n += 1
#         S = S.strip(S[n])
#     else:
#         print(0)
#         break

#     if S.index(S[n]) and S.index(S[-n-1]) == (len(S) +1 ) / 2:
#         print(1)
#         break

# 어떤게 잘못된 걸까

# 다른사람 코드
word = 'level'
# 값 초기화
# start : 0
# end : len(word) - 1
# while
# start 값이 end보다 작을때
n = 0
end = len(word) - 1
is_pal = True
while n < end:
    if word[n] != word[end]:
        is_pal = False
        break
    n += 1
    end -= 1
        
if is_pal:
    print(1)
else:
    print(0)


# 2789번 유학금지
# 이메일의 각 단어중 CAMBRIDGE에 포함된 알파벳 모두 삭제하기
# ex) LOVA -> LOV

S = input()

S_list = []
for i in S:
    if i not in 'CAMBRIDGE':
        S_list.append(i)

print(*S_list, sep='')


# 2675번 문자열 반복
# 문자열 S를 받을때 P번 반복해서 새 문자열 P를 만든후 출력

T = int(input())

for t in range(T):
    N, S = input().split()
    S_list = []
    for i in S:
        S_list.append(i*int(N))
    print(*S_list, sep='')


# 17249번 태보태보 총난타

S = input()
print(S[:S.index('(')].count('@'), S[S.index(')'):].count('@'), sep=' ')


# 2941 크로아티아 알파벳
S = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croatia:
    S = S.replace(i, '1')

print(len(S))


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