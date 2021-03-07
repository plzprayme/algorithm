import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (x, y, w, h) = readLine().split(" ").map { it.toInt() }
    print(minOf(x, y, w-x, h-y))
}