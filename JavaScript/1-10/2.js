const readline = require('readline');

let rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
});

function findMultipleofBothThreeAndFour(start, end) {
    resultList = [];
    for (let number = start; number <= end; number++) {
        if (number % 3 === 0 && number % 4 === 0) {
            resultList.push(number);
        }
    }

    console.log(`The result is [${resultList}]`);
}

function main() {
    rl.question("Enter the starting number: ", (start) => {
        rl.question("Enter the ending number: ", (end) => {
            findMultipleofBothThreeAndFour(parseInt(start), parseInt(end));
            rl.close();
        });
    });
}

main();