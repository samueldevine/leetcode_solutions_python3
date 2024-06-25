from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        left_pointer = 0
        for num in nums:
            if num != val:
                nums[left_pointer] = num
                left_pointer += 1

        return left_pointer


"""
Process:
Use two pointers, Left and Right
- Right pointer will scan through the array on each loop. Implied in for loop
- Left pointer will indicate where the next unique value should be placed
    Left pointer can also tell us how many unique values we've seen at the end

O(n) time to scan through nums
O(1) space, only need to store pointer variable



diagram for example [3, 2, 2, 3], val = 3

loop 0
[3,  2,  2,  3]
[RL, _,  _,  _]

loop 1
[3 , 2,  2,  3]
[L , R,  _,  _]
[2 , 2,  2,  3] assign R val to L position
[_ ,RL,  _,  _] increment L pointer

loop 2
[2 , 2,  2,  3]
[_ , L,  R,  _]
[2 , 2,  2,  3] assign R value to L position (array is unchanged in this case)
[_ , _, RL,  _] increment L pointer

loop 3
[2 , 2,  2,  3]
[_ , _,  L,  R]

return L   two unique values are left at indices 0 through 1 (inclusive)
"""
