const isUnique = arr => {
  let unique = true;

  for (let i = 0; i < arr.length; i++) {
    console.log(`~~~~ ** OUTER LOOP ** ~~~~ * i * === ${i}`);

    for (let j = 0; j < arr.length; j++) {
      console.log(`~~~~ INNER LOOP ~~~~ j === ${j}`);
      if (i !== j && arr[i] === arr[j]) {
        unique = false;
      }
    }
  }

  return unique;
};

console.log(isUnique([1, 2, 3]) === true);
console.log(isUnique([1, 1, 3]) === false);
