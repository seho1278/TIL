# 9012번 괄호

# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 '('와 ')'만으로 구성되어 있는 문자열이다.
# 괄호의 모양이 바르게 구성된 문자열은 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 "()"문자열은 기본 VPS이라고 부른다
# 만일 x가 VPS라면 이것을 하나의 괄호에 넣은 새로운 문자열"(x)"도 VPS가 된다.
# 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다

# 입력 : 입력 데이터는 표준 입력을 사용 T개의 테스트 데이터로 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한줄에 주어진다.

T = int(input())

for t in range(T):
    result = []
    S = input()
    VPS = True
    for s in S:
        if s == '(':
            result.append(s)
        elif s == ')':
            if '(' in result:
                result.pop()
            else:
                print('NO')
                VPS = False
                break
    
    if len(result) == 0 and VPS:
        print('YES')
    elif VPS:
        print('NO')
