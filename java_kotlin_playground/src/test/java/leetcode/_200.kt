package leetcode

class _200 {
    private var row = 0;
    private var col = 0;

    fun numIsLands(grid: Array<CharArray>): Int {
        val answer = 0
        row = grid.size
        col = grid[0].size

        grid.forEachIndexed { y, row ->
            row.forEachIndexed { x, value ->
                if (value == '1') moveTo(grid, y, x)
            }
        }

        return answer
    }

    private fun moveTo(grid: Array<CharArray>, y: Int, x: Int) {
        if (row == this.row || row == -1 ||
            col == this.col || col == -1 ||
            grid[row][col] != '1'
        ) {
            return
        }

        grid[row][col] = 'X'

        moveTo(grid, row + 1, col)
        moveTo(grid, row, col + 1)
        moveTo(grid, row - 1, col)
        moveTo(grid, row, col - 1)
    }
}