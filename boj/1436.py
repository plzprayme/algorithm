
import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        N = input()
        if N == "1":
            return "666"
        
        N = str(int(N) - 1)
        cnt = N.count('6')
        if cnt >= 3:
            return N

        six = ''
        if cnt >= 3:
            return N
        else:
            return N + ('6' * (3 - cnt))

        # return "666" if N == "1" else str(int(N)-1) + "666"

print(Solution().solution())