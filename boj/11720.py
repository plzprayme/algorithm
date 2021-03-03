import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        N = int(input())
        result = 0
        for i in input():
            result += int(i)
        return result
        
print(Solution().solution())