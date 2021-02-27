# 문제 #
# 연속된 O의 개수가 점수가 된다
# OOXXOXXOOO
# 1200100123

# 입력 #
# 테스트 케이스 개수
# 0보다 크고 80보다 작은 O와 X로 이루어진 문자열

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        result = 0
        for i in range(int(input())):
            result = cnt = 0

            for i in input():
                if i == 'O':
                    cnt += 1
                    result += cnt
                    continue
        
                cnt = 0
            print(result)
        

Solution().solution()