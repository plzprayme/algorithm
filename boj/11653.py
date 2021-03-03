import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        N = int(input())
        
        num = 2
        while N != 1:
            if N % num == 0:
                N //= num
                print(num)
                continue
            num += 1
        
Solution().solution()