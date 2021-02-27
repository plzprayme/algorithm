# 문제 #
# 윤년일 때는 1, 아니면 0을 출력
# 윤년은 연도가 4의 배수이면서 100의 배수가 아닐 때 또는 400의 배수일 때 이다.

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        year = int(input())
        if year % 400 == 0:
            return 1
        
        if year % 4 == 0 and year % 100 != 0:
            return 1
        
        return 0

            

print(Solution().solution())
