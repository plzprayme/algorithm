from typing import List


class Solution:
    row = 0
    col = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        def move_to(_row, _col):
            if _row in (self.row, -1):
                return
            if _col in (self.col, -1):
                return
            if grid[_row][_col] != '1':
                return

            grid[_row][_col] = 'X'

            move_to(_row + 1, _col)  # 상
            move_to(_row, _col + 1)  # 우
            move_to(_row - 1, _col)  # 하
            move_to(_row, _col - 1)  # 좌

        answer = 0
        self.row, self.col = len(grid), len(grid[0])
        for r in range(self.row):
            for c in range(self.col):
                if grid[r][c] == '1':
                    answer += 1
                    move_to(r, c)

        return answer


print(Solution().numIslands(  # Output: 1
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
))

print(Solution().numIslands(  # Output: 3
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
))
