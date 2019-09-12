# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
	for i in range(len(array) - 1):
		firstNum = array[i]
		for j in range(i + 1, len(array)):
			secondNum = array[i + 1]
			if (firstNum + secondNum == targetSum):
				return [firstNum, secondNum]
	return []