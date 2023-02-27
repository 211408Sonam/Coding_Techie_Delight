"""

The longest alternating subsequence is a problem of finding a subsequence of a given sequence in which the elements are in alternating order and in which the sequence is as long as possible. In order words, we need to find the length of the longest subsequence with alternate low and high elements.

Input: [8, 9, 6, 4, 5, 7, 3, 2, 4]
Output: 6
Explanation: The longest alternating subsequence length is 6, and the subsequence is [8, 9, 6, 7, 3, 4] as (8 < 9 > 6 < 7 > 3 < 4).

Note that the longest alternating subsequence is not unique. Following are a few more subsequences of length 6:

(8, 9, 6, 7, 2, 4)
(8, 9, 4, 7, 3, 4)
(8, 9, 4, 7, 2, 4)

"""

def findLongestSequence(A, start, end, flag):
    result = 0
    for i in range(start, end + 1):
 
        if flag and A[i - 1] < A[i]:
            result = max(result, 1 + findLongestSequence(A, i + 1, end, not flag))
        elif not flag and A[i - 1] > A[i]:
            result = max(result, 1 + findLongestSequence(A, i + 1, end, not flag))
        else:
            result = max(result, findLongestSequence(A, i + 1, end, flag))
 
    return result
 
def longestSequence(A):
    if not A:
        return 0
    return 1 + max(findLongestSequence(A, 1, len(A) - 1, True),
                findLongestSequence(A, 1, len(A) - 1, False))
 
 
if __name__ == '__main__':
 
    A = [8, 9, 6, 4, 5, 7, 3, 2, 4]
 
    print('The length of the longest alternating subsequence is', longestSequence(A))
