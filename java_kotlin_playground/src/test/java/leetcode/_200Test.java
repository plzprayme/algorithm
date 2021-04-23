package leetcode;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class _200Test {
	private final _200 problem = new _200();

	@Test
	void case1() {
		char[][] case1 = {
			{'1', '1', '1', '1', '0'},
			{'1', '1', '0', '1', '0'},
			{'1', '1', '0', '0', '0'},
			{'0', '0', '0', '0', '0'}
		};

		assertEquals(problem.solution(case1), 1);
	}

	@Test
	void case2() {
		char[][] case2 = {
			{'1', '1', '0', '0', '0'},
			{'1', '1', '0', '0', '0'},
			{'0', '0', '1', '0', '0'},
			{'0', '0', '0', '1', '1'}
		};

		assertEquals(problem.solution(case2), 3);
	}
}