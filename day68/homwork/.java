function calculator() {
    const num1 = parseFloat(prompt("შეიყვანეთ პირველი რიცხვი:"));
    const num2 = parseFloat(prompt("შეიყვანეთ მეორე რიცხვი:"));
    const operation = prompt("შეიყვანეთ მოქმედების ტიპი (მიმატება, გამოკლება, გამრავლება, გაყოფა):");
    
    let result;

    switch(operation) {
        case 'მიმატება':
            result = num1 + num2;
            break;
        case 'გამოკლება':
            result = num1 - num2;
            break;
        case 'გამრავლება':
            result = num1 * num2;
            break;
        case 'გაყოფა':
            result = num1 / num2;
            break;
        default:
            alert("არასწორი ოპერაცია.");
            return;
    }
    console.log(`შედეგი: ${result}`);
}

function sumOfNumbers(numbers) {
    let sum = 0;
    for (let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }
    return sum;
}

function averageOfNumbers(numbers) {
    const sum = sumOfNumbers(numbers);
    return sum / numbers.length;
}

function evenOrOdd() {
    const number = parseInt(prompt("შეიყვანეთ რიცხვი:"));
    if (number % 2 === 0) {
        console.log(`${number} არის ლუწი`);
    } else {
        console.log(`${number} არის კენტი`);
    }
}

function timeTravel() {
    const currentAge = parseInt(prompt("რა ასაკი გაქვთ?"));
    const currentYear = parseInt(prompt("რომელი წელია ახლა?"));
    const travelYears = parseInt(prompt("რამდენი წელით გსურთ მოგზაურობა დროში?"));
    const direction = prompt("წარსულში გსურთ მოგზაურობა თუ მომავალში? (მომავალი/წარსული)");

    let newYear;
    let newAge;

    if (direction === "მომავალი") {
        newYear = currentYear + travelYears;
        newAge = currentAge + travelYears;
    } else if (direction === "წარსული") {
        newYear = currentYear - travelYears;
        newAge = currentAge - travelYears;
    } else {
        console.log("არასწორი მიმართულება.");
        return;
    }

    console.log(`დროში მოგზაურობის შემდეგ წელი იქნება: ${newYear}, და თქვენ იქნებით: ${newAge} წლის.`);
}

// გამოსახვა (შეგიძლიათ ყველა ფუნქცია ცალ-ცალკე ამოიძახოთ)

calculator();                // 1) კალკულატორი
console.log(`რიცხვების ჯამი: ${sumOfNumbers([10, 20, 30, 40])}`); // 2) ჯამი
console.log(`რიცხვების საშუალო არითმეტიკული: ${averageOfNumbers([10, 20, 30, 40])}`); // 3) საშუალო
evenOrOdd();                 // 4) კენტი ან ლუწი
timeTravel();                // 5) დროში მოგზაურობა
