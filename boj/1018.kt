    val (N, M) = readLine().split(" ").map { it.toInt() }
    val wood: List<String> = readLines()

    val W = "WBWBWBWB"
    val B = "BWBWBWBW"

    val white = arrayOf(
        W,B,W,B,W,B,W,B
    )
    val black = arrayOf(
        B,W,B,W,B,W,B,W
    )

    fun window(r: Int, c: Int, mask: Array<String>): Int {
        var updated = 0
        for (i in r until r+8) {
            for (j in c until c+8) {
                if (wood[i][j] != mask[i-r][j-c]) {
                    updated += 1
                }
            }
        }
        return updated
    }

    var answer = Int.MAX_VALUE
    for (i in 0 until N-7) {
        for (j in 0 until M-7) {
            answer = min(answer, window(i, j, white))
            answer = min(answer, window(i, j, black))
        }
    }

    print(answer)