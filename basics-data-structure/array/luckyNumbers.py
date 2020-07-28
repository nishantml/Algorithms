"""
1380. Lucky Numbers in a Matrix

Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.



Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]

"""

from typing import List


class Solution:
    def getCol(self, matrix: List[List[int]], col: int) -> List[int]:
        return [sub[col] for sub in matrix]

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minV = []
        maxV = []
        for i in range(len(matrix)):
            minV.append(min(matrix[i]))

        for j in range(len(matrix[0])):
            maxV.append(max(self.getCol(matrix, j)))

        return set(minV).intersection(set(maxV))
