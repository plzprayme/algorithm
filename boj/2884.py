# 문제 #
# 주어진 시간보다 알람을 45분 일찍 맞추기

# 입력 #
# 0 <= H <= 23 / 0 <= M <= 59

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        H, M = map(int, input().split())
        _H, _M = range(24), range(60)
        
        if M - 45 < 0:
            H = H - 1
        
        print(_H[H], _M[M-45], sep=' ')
        

Solution().solution()