// 1. რა არის let?
// 'let' საშუალებას გვაძლევს ცვლადის დეკლარაცია ბლოკის შიგნით.
let a = 10;
console.log(a); // პასუხი: 10

// 2. რა არის const?
// 'const' ნიშნავს, რომ ცვლადის მნიშვნელობა ვერ შეიცვლება ინიციალიზაციის შემდეგ.
const b = 5;
console.log(b); // პასუხი: 5

// 3. რა განსხვავებაა let და var შორის?
// 'var' არის ფუნქციის შიგნით ლოკალური, 'let' კი ბლოკის შიგნით ლოკალური.
var c = 20;
if (true) {
  let c = 30;
  console.log(c); // პასუხი: 30 (let-ის ბლოკის შიგნითა მნიშვნელობა)
}
console.log(c); // პასუხი: 20 (var-ის გლობალური მნიშვნელობა)

// 4. რა არის ფუნქცია?
// ფუნქცია არის კოდის ბლოკი, რომელიც ასრულებს გარკვეულ მოქმედებას.
function add(x, y) {
  return x + y;
}
console.log(add(3, 7)); // პასუხი: 10

// 5. რა არის callback ფუნქცია?
// callback არის ფუნქცია, რომელიც გადაეცემა სხვა ფუნქციას არგუმენტად.
function doSomething(value, callback) {
  callback(value * 2);
}
doSomething(5, function(result) {
  console.log(result); // პასუხი: 10
});

// 6. რა არის undefined?
// ცვლადი, რომელიც დეკლარირებულია მაგრამ არა ინიციალიზებული, იღებს undefined მნიშვნელობას.
let d;
console.log(d); // პასუხი: undefined

// 7. რა არის null?
// null არის მიზანმიმართულად მინიჭებული სიცარიელე.
let e = null;
console.log(e); // პასუხი: null

// 8. რა არის NaN?
// NaN ნიშნავს "Not-a-Number", გამოიყენება, როდესაც რიცხვი არ არის ვალიდური.
let f = "text" / 2;
console.log(f); // პასუხი: NaN

// 9. რა განსხვავებაა == და === შორის?
// == მხოლოდ მნიშვნელობას ადარებს, ხოლო === ასევე ტიპს ამოწმებს.
console.log(5 == '5'); // პასუხი: true (ტიპი არ მოწმდება)
console.log(5 === '5'); // პასუხი: false (ტიპიც მოწმდება)

// 10. რა არის ობიექტი?
// ობიექტი არის მონაცემთა სტრუქტურა, რომელსაც აქვს თვისებები.
let car = { brand: "BMW", model: "M3", year: 2021 };
console.log(car.model); // პასუხი: M3

// 11. როგორ დავამატოთ თვისება ობიექტს?
// ობიექტს შეგვიძლია ახალი თვისება დავამატოთ წერტილის ნოტაციით.
car.color = "blue";
console.log(car.color); // პასუხი: blue

// 12. როგორ შევცვალოთ ობიექტის თვისება?
// ობიექტის თვისებების შეცვლა შესაძლებელია.
car.year = 2022;
console.log(car.year); // პასუხი: 2022

// 13. როგორ წავშალოთ ობიექტის თვისება?
// delete ოპერატორით შესაძლებელია ობიექტის თვისების წაშლა.
delete car.model;
console.log(car.model); // პასუხი: undefined

// 14. რა არის მასივი?
// მასივი არის მონაცემთა სტრუქტურა, რომელიც ინახავს ელემენტების კოლექციას.
let colors = ["red", "green", "blue"];
console.log(colors[1]); // პასუხი: green

// 15. როგორ დავამატოთ ელემენტი მასივს?
// push() მეთოდი მასივში ახალ ელემენტს ამატებს.
colors.push("yellow");
console.log(colors); // პასუხი: ["red", "green", "blue", "yellow"]

// 16. როგორ წავშალოთ ელემენტი მასივიდან?
// pop() მეთოდი შლის ბოლო ელემენტს.
colors.pop();
console.log(colors); // პასუხი: ["red", "green", "blue"]

// 17. როგორ ვიპოვოთ მასივის სიგრძე?
// length თვისება გვიჩვენებს მასივის ელემენტების რაოდენობას.
console.log(colors.length); // პასუხი: 3

// 18. როგორ შევამოწმოთ მასივი ცარიელია თუ არა?
// მასივის length თუ 0-ია, ის ცარიელია.
console.log(colors.length === 0); // პასუხი: false

// 19. რა არის ციკლი for?
// for ციკლი განმეორებით ასრულებს მოქმედებებს მოცემულ რაოდენობის ჯერ.
for (let i = 0; i < colors.length; i++) {
  console.log(colors[i]);
}

// 20. რა არის while ციკლი?
// while ციკლი ასრულებს მოქმედებებს მანამ, სანამ პირობა მართალია.
let g = 0;
while (g < 3) {
  console.log(g);
  g++;
}

// 21. რა არის if-else სტრუქტურა?
// if-else სტრუქტურა იყენებს პირობას, რათა მიიღოს გადაწყვეტილება.
let h = 10;
if (h > 5) {
  console.log("h მეტია 5-ზე");
} else {
  console.log("h ნაკლებია ან ტოლია 5-ის");
}

// 22. რა არის switch?
// switch სტრუქტურა იყენებს მრავალი შემთხვევის შესამოწმებლად.
let day = 3;
switch(day) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  default:
    console.log("Invalid day");
}

// 23. რა არის ტერნარული ოპერატორი?
// ტერნარული ოპერატორი არის მოკლე if-else კონსტრუქცია.
let age = 18;
let canVote = age >= 18 ? "Yes" : "No";
console.log(canVote); // პასუხი: Yes

// 24. რა არის ფუნქცია გამოძახებით (self-invoking function)?
// ფუნქცია, რომელიც თვითონვე იძახებს.
(function() {
  console.log("ეს ფუნქცია თვითონვე იძახებს");
})();

// 25. როგორ ვაბრუნებთ მნიშვნელობას ფუნქციიდან?
// return ოპერატორი ფუნქციიდან აბრუნებს შედეგს.
function square(x) {
  return x * x;
}
console.log(square(4)); // პასუხი: 16

// 26. როგორ გამოვიძახოთ ფუნქცია?
// ფუნქციის სახელის შემდეგ სქობებით შეგვიძლია მისი გამოძახება.
function greet() {
  console.log("Hello!");
}
greet(); // პასუხი: Hello!

// 27. რა არის arrow function?
// arrow function არის მოკლე ფორმა ფუნქციის დეკლარაციის.
let multiply = (x, y) => x * y;
console.log(multiply(3, 4)); // პასუხი: 12

// 28. რა არის async ფუნქცია?
// async ფუნქცია გამოიყენება ასინქრონული კოდის გასამართავად.
async function fetchData() {
  return "Data fetched!";
}
fetchData().then(console.log); // პასუხი: Data fetched!

// 29. რა არის პრომისი (Promise)?
// პრომისი გამოიყენება ასინქრონული ოპერაციისთვის.
let promise = new Promise((resolve, reject) => {
  let success = true;
  if (success) {
    resolve("Operation succeeded");
  } else {
    reject("Operation failed");
  }
});
promise.then(console.log).catch(console.error);

// 30. როგორ გამოვიყენოთ try-catch?
// try-catch გამოიყენება შეცდომების დასაჭერად.
try {
  throw new Error("Something went wrong");
} catch (error) {
  console.error(error.message); // პასუხი: Something went wrong
}

// 31. როგორ გამოვიყენოთ forEach?
// forEach მეთოდი მასივზე მოქმედებს ელემენტების გავლით.
colors.forEach((color) => console.log(color));

// 32. რა არის map მეთოდი?
// map მეთოდი ქმნის ახალ მასივს, თითოეული ელემენტის ტრანსფორმაციით.
let numbers = [1, 2, 3, 4];
let doubled = numbers.map((num) => num * 2);
console.log(doubled); // პასუხი: [2, 4, 6, 8]

// 33. რა არის filter მეთოდი?
// filter ქმნის ახალ მასივს იმ ელემენტებით, რომლებიც აკმაყოფილებენ პირობას.
let evenNumbers = numbers.filter((num) => num % 2 === 0);
console.log(evenNumbers); // პასუხი: [2, 4]

// 34. რა არის reduce მეთოდი?
// reduce გამოიყენება მასივის ელემენტების დასაყვანად ერთ მნიშვნელობამდე.
let sum = numbers.reduce((total, num) => total + num, 0);
console.log(sum); // პასუხი: 10

// 35. რა არის JSON?
// JSON არის მონაცემთა ფორმატი, რომელიც გამოიყენება მონაცემების გაცვლისთვის.
let jsonString
// 36. როგორ გადავაქციოთ ობიექტი JSON-ში?
// JSON.stringify() გამოიყენება ობიექტის JSON ფორმატში გადაყვანისთვის.
let person = { name: "Anna", age: 25 };
let jsonStr = JSON.stringify(person);
console.log(jsonStr); // პასუხი: '{"name":"Anna","age":25}'

// 37. რა არის localStorage?
// localStorage საშუალებას გვაძლევს ბრაუზერში დავმახსოვროთ მონაცემები, რომლებიც გრძელდება გვერდების ჩატვირთვამდე.
localStorage.setItem("username", "user1");
console.log(localStorage.getItem("username")); // პასუხი: user1

// 38. რა არის sessionStorage?
// sessionStorage მუშაობს იგივე პრინციპით, როგორც localStorage, მაგრამ მონაცემები ნულდება როცა ტაბი იხურება.
sessionStorage.setItem("sessionID", "abc123");
console.log(sessionStorage.getItem("sessionID")); // პასუხი: abc123

// 39. რა არის AJAX?
// AJAX (Asynchronous JavaScript and XML) არის ტექნოლოგია, რომელიც საშუალებას გვაძლევს ასინქრონულად მივიღოთ მონაცემები სერვერიდან.
let xhr = new XMLHttpRequest();
xhr.open("GET", "https://api.example.com/data", true);
xhr.onload = function () {
  if (xhr.status === 200) {
    console.log("Data received:", xhr.responseText);
  }
};
xhr.send(); // პასუხი: ასინქრონულად მიღებული მონაცემები

// 40. როგორ გამოვიყენოთ fetch?
// fetch არის უფრო მარტივი გზა ასინქრონულად მონაცემების მოსაძებნად.
fetch("https://api.example.com/data")
  .then((response) => response.json())
  .then((data) => console.log(data));

// 41. რა განსხვავებაა synchronous და asynchronous კოდებს შორის?
// სინქრონული კოდი ასრულებს თითოეულ ოპერაციას ქვე-ქვე, ასინქრონული კოდი არ აჩერებს პროგრამის შესრულებას.
console.log("Start");
setTimeout(() => console.log("Async call"), 1000); // ასინქრონული ოპერაცია
console.log("End"); // პასუხი: Start, End, Async call (მოწოდების შემდეგ)

// 42. რა არის კლასი (class)?
// კლასი არის ობიექტის შაბლონი, რომელიც იძლევა ობიექტების შექმნას.
class Car {
  constructor(brand, model) {
    this.brand = brand;
    this.model = model;
  }
  details() {
    return `${this.brand} ${this.model}`;
  }
}
let car1 = new Car("BMW", "X5");
console.log(car1.details()); // პასუხი: BMW X5

// 43. როგორ შევქმნათ ობიექტის ინსტანცია?
// new ოპერატორით შეგვიძლია შევქმნათ კლასის ახალი ინსტანცია.
let car2 = new Car("Audi", "A4");
console.log(car2.details()); // პასუხი: Audi A4

// 44. რა არის მოდულები (modules)?
// მოდულები საშუალებას გვაძლევს დავყოთ კოდი სხვადასხვა ფაილებში და გამოვიყენოთ იმპორტით.
export function sayHello() {
  return "Hello, World!";
}

// 45. როგორ გამოვიყენოთ მოდულები JavaScript-ში?
// import გვაძლევს საშუალებას შევიტანოთ მოდული სხვა ფაილიდან.
import { sayHello } from './module.js';
console.log(sayHello()); // პასუხი: Hello, World!

// 46. როგორ შევამოწმოთ ცვლადი არის თუ არა რიცხვი?
// isNaN() ფუნქცია გამოიყენება, რათა შევამოწმოთ, არის თუ არა მნიშვნელობა რიცხვი.
let number = 42;
console.log(isNaN(number)); // პასუხი: false

// 47. როგორ შევქმნათ თარიღი (Date) ობიექტი?
// Date ობიექტი გამოიყენება დროისა და თარიღის დასამუშავებლად.
let today = new Date();
console.log(today); // პასუხი: მიმდინარე თარიღი და დრო

// 48. როგორ დავაყენოთ სესიაზე დროის შეზღუდვა?
// setTimeout() ფუნქციას ვაძლევთ დროს, რამდენ ხანში უნდა შესრულდეს.
setTimeout(() => {
  console.log("This message appears after 3 seconds");
}, 3000); // პასუხი: ეს შეტყობინება გამოჩნდება 3 წამში

// 49. როგორ შევაჩეროთ განმეორებითი ოპერაცია?
// setInterval() ქმნის განმეორებით ციკლს, ხოლო clearInterval() აჩერებს მას.
let interval = setInterval(() => {
  console.log("Repeating every 2 seconds");
}, 2000);
setTimeout(() => clearInterval(interval), 7000); // 7 წამში შეჩერდება

// 50. როგორ გამოვიყენოთ Math ობიექტი?
// Math ობიექტი გვაძლევს რიცხვითი ოპერაციების შესრულების ფუნქციებს.
console.log(Math.max(5, 10, 15)); // პასუხი: 15 (მაქსიმალური მნიშვნელობა)
console.log(Math.random()); // პასუხი: რენდომული რიცხვი 0-დან 1-მდე