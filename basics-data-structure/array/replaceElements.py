"""
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newLst = []
        for i in range(len(arr) - 1):
            maxVal = 0
            for j in range(i + 1, len(arr)):
                if maxVal < arr[j]:
                    maxVal = arr[j]
            newLst.append(maxVal)
            # print(maxVal)
        newLst.append(-1)
        return newLst

    def replaceElements1(self, arr: List[int]) -> List[int]:
        """ Optimal Solution """
        if len(arr) == 1:
            return [-1]
        newLst = []
        newLst.append(max(arr[1:]))
        for i in range(1, len(arr) - 1):
            # print(max(arr[i+1:]))
            newLst.append(max(arr[i + 1:]))
        newLst.append(-1)
        return newLst
