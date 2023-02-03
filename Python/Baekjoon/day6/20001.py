#20001번 고무오리 디버깅

S = input()

problem = []

while True:
    S2 = input()

    if S2 == '문제':
        problem.append(S2)
        
    elif S2 == '고무오리':
        if problem:
            problem.pop(0)
        else:
            problem.append('문제')
            problem.append('문제')

    elif S2 == '고무오리 디버깅 끝':
        break

if len(problem) == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')