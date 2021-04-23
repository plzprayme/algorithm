
import sys
class Solution:
    input = lambda: sys.stdin.readline
    def solution(self):
        already, need = map(int, input().split())
        rj45s = [int(input()) for i in range(already)]
        length = sum(rj45s) // need

        if already == need:
            return min(rj45s)

        while True:
            if need == sum([rj45 // length for rj45 in rj45s]):
                return length

            length -= 1


# 4 11
# 802
# 743
# 457
# 539
print(Solution().solution())