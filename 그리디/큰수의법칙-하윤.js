const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

const question = (q = '') => new Promise( (resolve) => rl.question(q, resolve));

async function main() {
    let [n, m, k] = (await question()).split(' ').map( s => Number(s));
    let l = (await question()).split(' ').map( s => Number(s)).sort( (a,b) => b-a);

    let count = 0;
    let result = 0;
    while (m-- !== 0) {
        if (count !== k) {
            count++;
            result += l[0];
        } else {
            count = 0;
            result += l[1];
        }
    }
    console.log(result);
}
main().then();