# 2789번 유학금지
# 이메일의 각 단어중 CAMBRIDGE에 포함된 알파벳 모두 삭제하기
# ex) LOVA -> LOV

S = input()

S_list = []
for i in S:
    if i not in 'CAMBRIDGE':
        S_list.append(i)

print(*S_list, sep='')