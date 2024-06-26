from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        scanned_elements = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in scanned_elements:
                return [i, scanned_elements[complement]]
            else:
                scanned_elements[num] = i


"""
Process:
Create a hashtable to store values that have been previously scanned
    (this allows you to execute the loop only once, reducing time complexity
    at the cost of O(n) extra memory)
Scan through the input array nums and first calculate the "complement" that
would be requried to satisfy the condition
    - If the complement is already in the list of scanned elements, return its
    index along with the current number's index
    - If not, then add the current number and index to the hashtable and
    continue

O(n) time (iterate through the entire list once)
O(n) space (create a hashtable that stores the elements of the input array)
"""
