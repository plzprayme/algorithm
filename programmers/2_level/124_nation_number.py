
# 자연수만 존재한다.
# 124로만 표현한다



def digit_length(n):
    length = 0
    a = []
    while n:
        n //= 10
        a.append(n)
        print(a)
        length += 1
    a.append
    return length

def solution(n):
    answer = 11
    digit_length(answer)
    
    


        
    return answer

print(solution(4))