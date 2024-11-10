const readline = require('readline');

let rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
});


function main (numbers) {
    let sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    console.log(`The sum of the numbers is ${sum}`);
}

function askForNumbers() {
    let listNumbers = [];
    count = 0;

    if (count < 5) {
        rl.question("Enter a number : "), (number) => {
            listNumbers.push(parseInt(number));
            rl.close();
        }
        count++;
    }else {
        main(listNumbers);
    }


}

askForNumbers();