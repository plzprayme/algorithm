import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        # 0보다 크고 99보다 작거나 같은 정수가 주어진다.
        # 주어진 수가 10보다 작으면 0을 붙여서 두자리로 만들고 합한다.
        # 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어붙이면 새로운 수

        num = input()
        copy = num
        
        answer = 0
        # step 1 자리수 체크
        while True:
            print(copy, num)
            if len(copy) == 1:
                copy = '0' + copy
            
            weight = copy[1]
            copy = copy + str(int(copy[0]) + int(copy[1]))
            answer += 1
            
            if copy == num:
                return answer



print(Solution().solution())