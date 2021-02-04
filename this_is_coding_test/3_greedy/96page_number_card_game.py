# 여러 개의 숫자 카드 중에서
# 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임

# N X M (행, 열)
# 행을 먼저 선택한다. 
# 그 행에서 가장 낮은 숫자를 뽑는다.
# 각 행들에서 최솟값을 뽑은 후
# 그 최솟값들 중에서 가장 큰 값을 리턴한다.

def solution():
    m, n = map(int, input().split(" "))

    answer = float('-inf')
    for row in range(m):
        answer = max(answer, min(map(int, input().split(" "))))

    return answer

if __name__ == "__main__":
    print(solution())