def solution(participant, completion):
    sdict = {}
    for i in participant:
        if i in sdict:
            sdict[i] += 1
        else:
            sdict[i] = 1

    for i in completion:
        if sdict[i] == 1:
            del sdict[i]
        else:
            sdict[i] -= 1
    
    print((sdict.keys()))
    answer = list(sdict.keys())[0]
    return answer

# 얘는 같은 문자열 들어오면 처리 안됨
def solution2(p,c):
    p_sub_c = [x for x in p if x not in c]
    return p_sub_c

import collections

p = ['asdf','zxcv','qwer','tyui','tyui']
c = ['asdf','zxcv','qwer']

def countLettets(word):
    counter ={}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

def solution3(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def fibo(f,b):
    """
    피보나치 수열 시작 입력 2개는 일반적으로 0,1
    """
    front = f
    back  = b
    print(f"시작 값 1번째, 2번째 : {f}, {b}")
    result = 0
    def nacci(): # 클로저
        nonlocal front # 지역변수 변경 
        nonlocal back
        nonlocal result
        
        result = front + back
        front = back
        back = result
        return front, back, result

    return nacci


