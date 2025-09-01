const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


  
rl.question("Please enter number 1L: ", (num1) => {
  rl.question("Please enter number 2L: ", (num2) => {
    rl.question("Please enter the operation (+, -, *, /): ", (operation) => {
      let result;
      num1 = parseFloat(num1);
      num2 = parseFloat(num2);

      switch (operation) {
        case "+":
          result = num1 + num2;
          break;
        case "-":
          result = num1 - num2;
          break;
        case "*":
          result = num1 * num2;
          break;
        case "/":
          if (num2 === 0) {
            console.log("Error: Division by zero is not allowed.");
            rl.close();
            return;
          }
          result = num1 / num2;
          break;
        default:
          console.log("Error: Invalid operation.");
          rl.close();
          return;
      }

      console.log(`The result of ${num1} ${operation} ${num2} is: ${result}`);
      rl.close();
    });
  });
});
