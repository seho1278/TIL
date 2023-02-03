# 17249번 태보태보 총난타

S = input()
print(S[:S.index('(')].count('@'), S[S.index(')'):].count('@'), sep=' ')