# 2592번 대표값

list_ = [int(input()) for _ in range(10)]
dict_ = {}
for n in list_:
    if n not in dict_:
        dict_[n] = 1
    else:
        dict_[n] += 1
print(round(sum(list_)/len(list_)), max(dict_.items(), key=lambda x:x[1])[0] , sep='\n')