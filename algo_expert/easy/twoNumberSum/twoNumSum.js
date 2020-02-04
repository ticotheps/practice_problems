const myArr = [3, 5, -4, 8, 11, 1, -1, 6];

function twoNumSum(array, targetSum) {
	const numsCache = {};

	for (let i = 0; i < array.length; i++) {
		let potentialMatch = targetSum - array[i];

		if (potentialMatch in numsCache) {
			return [potentialMatch, array[i]];
		} else {
			numsCache[array[i]] = true;
		}
	}
	return [];
}

console.log(twoNumSum(myArr, 10));
