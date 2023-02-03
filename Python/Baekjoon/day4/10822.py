# 10822번 더하기
# 숫자와 콤마로만 이루어진 문자열 S에 포함되어 있는 자연수의 합 구하기
S = input()
print(sum(map(int, S.split(','))))