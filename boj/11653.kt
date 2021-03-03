import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    var N = nextInt()

    var num = 2
    while (N != 1) {
        if (N % num == 0) {
            N /= num
            println(num)
            continue
        }
        num += 1
    }

}