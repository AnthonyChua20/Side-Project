const readline = require( "readline");
function simpleInterest(principal, rate, time){
    return (principal * rate * time) /100;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter the principal amount: ", (principal) => {
  rl.question("Enter the rate of interest: ", (rate) => {
    rl.question("Enter the time in years: ", (time) => {
      const interest = simpleInterest(parseFloat(principal), parseFloat(rate), parseFloat(time));
      console.log(`The simple interest is: ${interest}`);
      rl.close();
    });
  });
});
