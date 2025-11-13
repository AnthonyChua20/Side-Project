function squareSum(numbers) {
  var square = 0;
  for (var i = 0; i < numbers.length; i++) {
    square += numbers[i] ** 2;
  }
  return square;
}

console.log(squareSum([1, 2, 3, 4, 5]));