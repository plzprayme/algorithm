

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        while True:
            a, b = map(int, input().split())
            if a == 0 and b == 0:
                break
            else:
                print(a+b)
            
            

Solution().solution()
