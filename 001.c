"""
Techie Delight: 


Given a set S of positive integers, determine if it can be partitioned into three disjoint subsets that all have the same sum, and they cover S.

Input: S = [7, 3, 2, 1, 5, 4, 8]
Output: True
Explanation: S can be partitioned into three partitions [[7, 3], [5, 4, 1], [8, 2]], each having a sum of 10.

Note that there can be multiple solutions to a single set.
    
"""

def subsetSum(S, n, a, b, c):

	if a == 0 and b == 0 and c == 0:
		return True
	if n < 0:
		return False

	A = False
	if a - S[n] >= 0:
		A = subsetSum(S, n - 1, a - S[n], b, c)
      
	B = False
	if not A and (b - S[n] >= 0):
		B = subsetSum(S, n - 1, a, b - S[n], c)
      
	C = False
	if (not A and not B) and (c - S[n] >= 0):
		C = subsetSum(S, n - 1, a, b, c - S[n])

	return A or B or C


def partition(S):

	if len(S) < 3:
		return False
    
	total = sum(S)
	return (sum(S) % 3) == 0 and subsetSum(S, len(S) - 1, total//3, total//3, total//3)


if __name__ == '__main__':

	S = [7, 3, 2, 1, 5, 4, 8]

	if partition(S):
		print('Set can be partitioned')
	else:
		print('Set cannot be partitioned')
