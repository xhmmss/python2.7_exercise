# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

def maxSequence(arr):

	result = 0
	if len(arr) > 0:
		if  max(arr) > 0:
			for i in range(len(arr)):
				for j in range(i+1,len(arr)+1):
					if sum(arr[i:j]) > result:
						result = sum(arr[i:j])

	return result

def maxSequence_clever(arr):

	result,tmp = 0,0
	for i in arr:
		tmp += i
		if tmp < 0:tmp = 0
		if tmp > result:result = tmp
	return result

print maxSequence_clever([-2, 1, -3, 4, -1, 2, 1, -5, 4])