var q = readLine()!.split(separator: " ").map { Int($0)! }
var l = readLine()!.split(separator: " ").map { Int($0)! }.sorted(by: {$0 > $1});

func main(q: [Int], l: [Int]) -> Void {
    var m = q[1]
    var count: Int = 0
    var result: Int = 0
    
    while m != 0 {
        if (count != q[2]) {
            count += 1
            result += l[0]
        } else {
            count = 0
            result += l[1]
        }
        m -= 1
    }
    print(result)
}
main(q: q, l: l)
