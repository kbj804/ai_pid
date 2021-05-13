def solution(participant, completion):
    hash = {}
    for i in participant:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    print(hash)
    for i in completion:
        if hash[i] == 1:
            del hash[i]
        else:
            hash[i] -= 1
    
    
    print((hash.keys()))
    answer = list(hash.keys())[0]
    return answer

def solution2(p,c):
    p_sub_c = [x for x in p if x not in c]
    return p_sub_c


p=['qwe','asd','zxc','vbn']
c=['qwe','asd','zxc']
print(solution(p,c))