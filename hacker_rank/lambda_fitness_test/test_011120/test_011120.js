function threeNumberSum(arr, target) {
	const tripletsArr = [];
	const arrLen = arr.length;
	console.log('arr = ', arr);
	console.log('target = ', target);

	for (let i = 0; i <= arrLen - 3; i++) {
		console.log(`\narr[${i}] = ${arr[i]}`);
		console.log(`arr[${i + 1}] = ${arr[i + 1]}`);
		console.log(`arr[${i + 2}] = ${arr[i + 2]}`);

		for (let j = i + 1; j <= arrLen - 3; j++) {
			console.log(`\narr[${j}] = ${arr[j]}`);
			console.log(`arr[${j + 1}] = ${arr[j + 1]}`);
			console.log(`arr[${j + 2}] = ${arr[j + 2]}`);

			for (let k = i + 2; k <= arrLen - 3; k++) {
				if (arr[i] !== arr[j] && arr[i] !== arr[k] && arr[j] !== arr[k]) {
					if (arr[i] + arr[j] + arr[k] === target) {
						let singleTripletArr = [arr[i], arr[j], arr[k]];
						tripletsArr.push(singleTripletArr);
					}
				}
			}
		}
	}

	return tripletsArr;
}

console.log(threeNumberSum([1, 2, 3, 4, 5], 8));
