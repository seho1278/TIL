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