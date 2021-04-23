package leetcode;

public class _200 {
	private int row;
	private int col;

	public int solution(char[][] grid) {
		int answer = 0;
		this.row = grid.length;
		this.col = grid[0].length;

		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (grid[i][j] == '1') {
					answer += 1;
					moveTo(grid, i, j);
				}
			}
		}

		return answer;
	}

	private void moveTo(char[][] grid, int row, int col) {
		if (row == this.row || row == -1 ||
			col == this.col || col == -1 ||
			grid[row][col] != '1') {
			return;
		}

		grid[row][col] = 'X';

		moveTo(grid, row + 1, col);
		moveTo(grid, row, col + 1);
		moveTo(grid, row - 1, col);
		moveTo(grid, row, col - 1);
	}
}
