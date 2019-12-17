const assert = require("assert");
(use strict);

function rand7(minNum, maxNum) {   
  const newMinNum = Math.ceil(minNum);
  const newMaxNum = Math.floor(maxNum);
  
  console.log("newMinNum = ", newMinNum);
  console.log("newMaxNum = ", newMaxNum);
  
  const randomNum = Math.ceil(Math.random() * ((newMaxNum - newMinNum) + newMinNum));
  
  return randomNum;
}

console.log(rand7(1, 7));  // should print an integer between 1 & 7
console.log(rand7(1, 7));
console.log(rand7(1, 7));
console.log(rand7(1, 7));
console.log(rand7(1, 7));
