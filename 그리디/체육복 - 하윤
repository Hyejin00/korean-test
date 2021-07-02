function solution(n, lost, reserve) {
    let count = n - lost.length;
    reserve.forEach(child => {
        let lend = lost.find( l => (child+1) === l || (child-1) === l);
        if (lend) {
            count++;
            lost.splice(lost.indexOf(lend), 1);
        }
    })
    return count;
}
