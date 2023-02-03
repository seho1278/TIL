# 1181번 단어 정렬

# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 길이가 짧은 것부터 길이가 같으면 사전순으로 정렬

# 입력 : 첫째 줄에 단어의 개수 N 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩

# import sys
# N = int(sys.stdin.readline())

# s_list = []
# for n in range(N):
#     s_list.append(input())

# s_list = set(s_list)    
# s_list = sorted(s_list)
# s_list = sorted(s_list, key=lambda x: len(x))

# print(*s_list, sep='\n')

# 다른사람 코드
N = int(input())
word_len = {}
for n in range(N):
    word = input()
    word_len[word] = len(word)

sorted_word_len = sorted(word_len.items(), key=lambda x:(x[1],x[0]))
for value in sorted_word_len:
    print(value[0])