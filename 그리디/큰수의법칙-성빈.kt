fun main() {
    val nmk = readLine()!!.split(" ").map { it.toInt() }
    val nums = readLine()!!.split(" ").map { it.toInt() }.sortedDescending()

    var result = 0
    var index = 0

    repeat(nmk[1]) {
        if (index < nmk[2]) {
            result += nums.first()
            index++
        } else {
            result += nums[1]
            index = 0
        }
    }

    println(result)
}
