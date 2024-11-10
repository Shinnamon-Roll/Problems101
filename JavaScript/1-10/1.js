const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function findMultiplesOfThree(startingNumber, endNumber) {
    let resultList = [];

    for (let result = startingNumber; result <= endNumber; result += 1) {
        if (result % 3 === 0 ) {
            resultList.push(result);
        }
    }

    console.log(`The results are : ${resultList}`)
}

function main() {
    rl.question("Enter the starting number: ", (startNumber) => {
        rl.question("Enter the ending number: ", (endNumber) => {
            findMultiplesOfThree(parseInt(startNumber), parseInt(endNumber));
            rl.close();
        });
    });
}

main();
