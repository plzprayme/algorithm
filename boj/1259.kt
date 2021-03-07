import java.io.BufferedReader
import java.io.InputStreamReader

 fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    while(true) {
        val word = readLine()
        if (word.equals("0")) {
            return
        }
        word.run {
            println(if(this == this.reversed()) "yes" else "no")
        }
    }
}