function countPositivesSumNegatives(input) {
  // your code here
  var negative = 0;
  var positive = 0;

  for (var i = 0; i < input.length; i++) {
    if (input[i] > 0) {
      positive++;
    } else if (input[i] < 0) {
      negative += input[i];
    }
  }
  return [positive, negative];
}

console.log(
  countPositivesSumNegatives([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15,
  ])
);
