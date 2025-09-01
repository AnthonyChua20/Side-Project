const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


monthDays = new Map();
monthDays.set("january", 31)
monthDays.set("febuary", 28)
monthDays.set("march", 31)
monthDays.set("april", 30)
monthDays.set("may", 31)
monthDays.set("june", 30)
monthDays.set("july", 31)
monthDays.set("august", 31)
monthDays.set("september", 30)
monthDays.set("october", 31)
monthDays.set("november", 30)
monthDays.set("december", 31)
/*
Concession cost for Adults = $128
Workfare Transport Scheme = $128 - $32 = $96
Train Concession for students = $48
Bus Concession for students = $55.50
Hybrid Concession for students = $81
Bus Fee up to 3.2km = $1.19
3.3km - 4.2km = $1.29
4.3km - 5.2km = $1.40
5.3km - 6.2km = $1.50
6.3km - 7.2km = $1.59
6.3km - 8.2km = $1.66
8.3km - 9.2km = $1.73
9.3km - 10.2km = $1.81
Mrt fee up to 3.2km = $0.69


logic flow for concession calculator:
1. user input month
2. user input adult or student
3. if user is adult do they have workfare transport scheme
4. if user is student do they want train, bus or hybrid
5. take concession price and divde it by the amount of days in the month to get daily prices
6. take daily price and calculate for the number of days in the month
7. how many trips do the user have to take in a month to make it worth it
8. is it worth it for the user to get the concession
9. Advance(distance based)
*/


rl.question("Enter the month: ", (month) => {
  month = month.toLowerCase();

  rl.question("Are you an adult or a student? ", (userType) => {
    userType = userType.toLowerCase();

    if (userType === "adult") {
      rl.question("Do you have the Workfare Transport Scheme? (yes/no): ", (hasWorkfare) => {
        hasWorkfare = hasWorkfare.toLowerCase();
        let concessionPrice = hasWorkfare === "yes" ? 96 : 128;
        // let dailyConcessionPrice = concessionPrice / monthDays.get(month);
        let dailyPrice = 0.69;
        let totalPrice = (Math.ceil(dailyPrice * monthDays.get(month))) * 2;
        let breakEvenTrips = Math.ceil(concessionPrice / dailyPrice);
        breakEvenTrips = breakEvenTrips / monthDays.get(month);

        console.log(`You need to make at least ${breakEvenTrips} trips in ${month} per day to make the concession worth it or it would be $${totalPrice} for the month with 2 trip per day`);

        rl.close();
      });
    } else {
      rl.question("Do you want train, bus or hybrid concession? ", (transportType) => {
        transportType = transportType.toLowerCase();

        let concessionPrice;
        switch (transportType) {
          case "train":
            concessionPrice = 48;
            break;
          case "bus":
            concessionPrice = 55.50;
            break;
          case "hybrid":
            concessionPrice = 81;
            break;
        }

        let dailyPrice = 0.52;
        // let dailyConcessionPrice = concessionPrice / monthDays.get(month);
        let breakEvenTrips = Math.ceil(ConcessionPrice / dailyPrice);

        console.log(`You need to make at least ${breakEvenTrips} trips in ${month} to make the concession worth it.`);

        rl.close();
      });
    }
  });
});
