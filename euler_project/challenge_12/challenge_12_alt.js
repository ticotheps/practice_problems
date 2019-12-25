const triNumFactorsCache = {};

function findTriNum(minNumDivisors) {
  console.log(triNumFactorsCache);
  let currentTriNum = 0;
  const reallyBigNum = Number.MAX_SAFE_INTEGER;

  for (let i = 1; i < reallyBigNum; i++) {
    currentTriNum += i; 
    console.log("currentTriNum = ", currentTriNum);

    return currentTriNum;
  }

  return minNumDivisors;
}

console.log(findTriNum(4));