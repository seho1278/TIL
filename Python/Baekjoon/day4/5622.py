# 5622번 다이얼
# 숫자를 하나 누를 때 마다 다이얼이 처음위치로 돌아간다
# 숫자 1을 걸려면 총 2초 필요, 한칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다.
# 할머니가 외운 단어가 주어졌을 때 전화를 걸기 위해 필요한 최소 시간을 구하는 프로그램 작성

# 입력 : 첫줄 알파벳 대문자 단어가 주어진다.
# 출력 : 첫줄에 다이얼을 걸기 위해 필요한 최소시간 출력

S = input()
dial = {
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10
}
d_list = []
for s in S:
    for key, value in dial.items():
        if s in key:
            d_list.append(value)

print(sum(d_list))