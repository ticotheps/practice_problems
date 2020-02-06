myArray = [3, 5, -4, 8, 11, 1, -1, 6];

# BRUTE FORCE SOLUTION - Nested "for" Loops
# Time Complexity = O(n^2)
# Space Complexity = O(1)
def twoNumberSum(array, targetSum):
  for i in range(len(array) - 1):
    firstNum = array[i]
    print('firstNum =', firstNum)
    
    for j in range(i + 1, len(array)):
      secondNum = array[j]

      if firstNum + secondNum == targetSum:
        return [firstNum, secondNum]
      
  return []

print(twoNumberSum(myArray, 10));

# SLIGHTLY OPTIMIZED SOLUTION - Sort & L+R Pointers
# Time Complexity = O(n log n)
# Space Complexity = O(n)
# function twoNumberSum(array, targetSum) {
# 	const sortedArray = array.sort((a, b) => a - b);
# 	console.log('sortedArray=', sortedArray);
# 	console.log('targetSum=', targetSum);

# 	let left = 0;
# 	let right = array.length - 1;

# 	while (left < right) {
# 		let currentSum = array[right] + array[left];
# 		console.log('currentSum=', currentSum);
# 		if (currentSum == targetSum) {
# 			return [array[right], array[left]];
# 		} else if (currentSum < targetSum) {
# 			left += 1;
# 			console.log('right = ', right);
# 		} else if (currentSum > targetSum) {
# 			right -= 1;
# 			console.log('left = ', left);
# 		}
# 	}
# 	return [];
# }

# const myArray = [3, 5, -4, 8, 11, 1, -1, 6];

# console.log(twoNumberSum(myArray, 10));

# MOST OPTIMAL SOLUTION - MEMOIZATION
# Time Complexity = O(n)
# Space Complexity = O(n)
# function twoNumberSum(array, targetSum) {
# 	const cache = {};

# 	for (let i = 0; i < array.length; i++) {
# 		let potentialMatch = targetSum - array[i];

# 		if (potentialMatch in cache) {
# 			return [potentialMatch, array[i]];
# 		} else {
# 			cache[array[i]] = true;
# 		}
# 	}
# 	return [];
# }
