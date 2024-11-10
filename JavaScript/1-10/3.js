const readline = require("readline");

let rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

function findNonMultiple(start, end) {
    resultList = [];
    for (let number = start; number <= end; number++) {
        if (number % 3 !== 0 && number % 4 !== 0 && number % 5 !== 0) {
            resultList.push(number);
        }
    }
    console.log(`The result is [${resultList}]`);
}

function main() {
    rl.question("Enter the starting number : ", (start) => {
        rl.question("Enter the ending number : ", (end) => {
            findNonMultiple(parseInt(start), parseInt(end));
            rl.close();
        });
    });
}

main();