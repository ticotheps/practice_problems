const maxArrayQueries = (n, queries) => {
  // console.log(n);
  // console.log(queries[0]);
  // console.log(queries[1]);
  // console.log(queries[2]);
  let initialZerosArray = [];
  let maximumValue = 0;

  for (let i = 0; i < n; i++) {
    initialZerosArray.push(0);
  }
  console.log(initialZerosArray);

  // for (let i = 0; i < queries.length; i++) {
  //   console.log(queries[i]);
  //   for (let j = 0; j < queries.length; j++) {
  //     console.log(queries[j]);
  //   }
  // }
  return maximumValue;
};

console.log(maxArrayQueries(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]));
