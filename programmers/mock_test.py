# 레벨 1 모의고사


def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    answer = [0, 0, 0]
    
    for i, v in enumerate(answers):
        if v == first[i % len(first)]:
            answer[0] += 1
        
        if v == second[i % len(second)]:
            answer[1] += 1
            
        if v == third[i % len(third)]:
            answer[2] += 1
            
            
    mx = max(answer)
    result = []
    for i, v in enumerate(answer):
        if mx == v:
            result.append(i+1)
    return result