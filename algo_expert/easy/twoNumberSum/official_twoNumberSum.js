// BRUTE FORCE SOLUTION - Nested "for" Loops
// Time Complexity = O(n^2)
// Space Complexity = O(1)
// function twoNumberSum(array, targetSum) {
// 	for (let i = 0; i < array.length - 1; i++) {
// 		let firstNum = array[i];

// 		for (let j = i + 1; j < array.length; j++) {
// 			let secondNum = array[j];

// 			if (firstNum + secondNum === targetSum) {
// 				return [firstNum, secondNum];
// 			}
// 		}
// 	}
// 	return [];
// }

// SLIGHTLY OPTIMIZED SOLUTION - Sorting & Pointers
// Time Complexity = O(n log n)
// Space Complexity = O(n)
function twoNumberSum(array, targetSum) {
	const cache = {};

	for (let i = 0; i < array.length; i++) {
		let potentialMatch = targetSum - array[i];

		if (potentialMatch in cache) {
			return [potentialMatch, array[i]];
		} else {
			cache[array[i]] = true;
		}
	}
	return [];
}

const myArray = [3, 5, -4, 8, 11, 1, -1, 6];

console.log(twoNumberSum(myArray, 10));

// MOST OPTIMAL SOLUTION - MEMOIZATION
// Time Complexity = O(n)
// Space Complexity = O(n)
// function twoNumberSum(array, targetSum) {
// 	const cache = {};

// 	for (let i = 0; i < array.length; i++) {
// 		let potentialMatch = targetSum - array[i];

// 		if (potentialMatch in cache) {
// 			return [potentialMatch, array[i]];
// 		} else {
// 			cache[array[i]] = true;
// 		}
// 	}
// 	return [];
// }

// const myArray = [3, 5, -4, 8, 11, 1, -1, 6];

// console.log(twoNumberSum(myArray, 10));
