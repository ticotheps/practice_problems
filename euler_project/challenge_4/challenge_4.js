const lowestNumByDigits = [0, 10, 100, 1000, 10000];
const highestNumByDigits = [9, 99, 999, 9999, 99999];

const findLargestPalindrome = numDigits => {
  const minimum = lowestNumByDigits[numDigits - 1];
  const maximum = highestNumByDigits[numDigits - 1];
  let largestPalindrome = 0;
  const productStringsArray = [];

  for (let i = minimum; i <= maximum; i++) {
    console.log('i = ', i);
    // let reversedProductString = [];
    let productString;
    for (let j = minimum; j <= maximum; j++) {
      console.log('j = ', j);
      let product = i * j;

      productString = product.toString();
      console.log('productString = ', productString);
      if (productString.length > 3) {
        productStringsArray.push(productString);
      }
    }
  }

  for (let k = 0; k < productStringsArray.length; k++) {
    let reversedProductString = [];
    for (let t = 0; t < productStringsArray[k][t]; t++) {
      reversedProductString.unshift(productStringsArray[k][t]);
      console.log(reversedProductString);
    }
    let reversedString = reversedProductString.join('');
    if (
      reversedProductString.length > 3 &&
      reversedString == productStringsArray[k]
    ) {
      largestPalindrome = reversedString;
    }
  }
  console.log('productStringsArray = ', productStringsArray);
  return largestPalindrome;
};

console.log(findLargestPalindrome(2));
