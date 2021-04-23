

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
    
        stack = [float('inf')]
    
        for i in range(int(input())):
            num = int(input())
            if stack[-1] >= num:
                print('+')
                stack.append(num)
                continue

            if stack[-1] 


                

        




print(Solution().solution())