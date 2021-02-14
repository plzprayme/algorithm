# 실패율
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

# 전체 스테이지 개수 N
# 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages

# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return


import collections
def solution(N, stages):
    challenging = collections.defaultdict(lambda: 0)
    clear = collections.defaultdict(lambda: 0)
    for i in stages:
        for j in range(1, i+1):
            if j == i:
                challenging[j] += 1   
            clear[j] += 1

    rate = {}
    for i in range(1, N+1):
        try:
            rate[i] = challenging[i]/clear[i]
        except:
            rate[i] = 1
    
    answer = []
    while rate:

        k, v = -1, -1
        for _k, _v in rate.items():
            if _v > v:
                v = _v
                k = _k
        answer.extend([k])
        rate.pop(k)
            

    return answer

print(solution(5, [2,1,2,6,2,4,3,3])) # 3,4,2,1,5
# print(solution(4, [4,4,4,4,4])) # 3,4,2,1,5