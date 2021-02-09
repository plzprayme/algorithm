# 레벨 1 예산

def solution(d, budget):
    # 신청 금액 d / 예산 budget
    # d의 길이 1 ~ 100 / 요소의 크기 1 ~ 100_000
    # budge의 크기 1 ~ 10_000_000
    
    count = 0
    for i in sorted(d):
        if budget < i:
            break
        budget -= i
        count += 1
    
    return count