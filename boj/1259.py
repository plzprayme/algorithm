import sys
import collections
class Solution:
    input = sys.stdin.readline
    def solution(self):
        while True:
            word = input() 
            if word == '0':
                return
            print('yes' if word == word[::-1] else 'no')            

Solution().solution()
