class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        var answer = 0
        val lostSet = lost.toHashSet()
        val reserveSet = reserve.toHashSet()
        (0 until n).forEach{ i ->
            val number = i + 1
            val hasLost = lostSet.contains(number)
            if(!hasLost){
                answer++
                return@forEach
            }

            val hasReserve = reserveSet.contains(number)
            if(hasReserve){
                reserveSet.remove(number)
                answer++
                return@forEach
            }

            if(this.canBorrow(number - 1, n, lostSet, reserveSet) || this.canBorrow(number + 1, n, lostSet, reserveSet)){
                answer++
                return@forEach
            }
        }
        return answer
    }

    fun canBorrow(number: Int, n: Int, lost: Set<Int>, reserve: MutableSet<Int>): Boolean{
        if(number <= 0 || number > n){
            return false
        }

        val hasReserve = reserve.contains(number)
        val hasLost = lost.contains(number)
        val canBorrow = !hasLost && hasReserve
        if(canBorrow){
            reserve.remove(number)
        }
        return canBorrow
    }
}
