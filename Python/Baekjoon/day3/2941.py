# 2941 크로아티아 알파벳
S = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croatia:
    S = S.replace(i, '1')

print(len(S))