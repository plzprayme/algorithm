import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    readLine()
    readLines()
        .toSortedSet()
        .sortedBy { it.length }
        .forEach { println(it) }
}
