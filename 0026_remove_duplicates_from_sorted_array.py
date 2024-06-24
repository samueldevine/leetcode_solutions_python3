"""
Process:
Use two pointers, Left and Right
- Right pointer will scan through the array on each loop. Implied in for loop
- Left pointer will indicate where the next unique value should be placed
    Left pointer can also tell us how many unique values we've seen at the end
- No need to start at 0 index, as that first value is guaranteed to be unique, so start at nums[1::]
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Base case: if array is len 0 or len 1, k is equal to the length and no modification is needed
        if len(nums) <= 1:
            return len(nums)

        left_pointer = 0
        for num in nums[1::]:
            if num != nums[left_pointer]:
                left_pointer += 1
                nums[left_pointer] = num

        return left_pointer + 1


"""
diagram for example [1, 1, 2]

loop 0
[1,  1,  2]
[RL, _,  _]

loop 1
[1 , 1,  2]
[L , R,  _]

loop 2
[1 , 1,  2]
[L , _,  R]
[->, L , R]  move left pointer before assigning new value
[1 , 2,  2]  assign new value to left pointer position

return L+1   two unique values are left at indices 0 through 1 (inclusive)
"""
