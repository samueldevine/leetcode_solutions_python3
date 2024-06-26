class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_str = str(x)
        right_pointer = len(x_str) - 1

        for char in x_str:  # see note below
            if char != x_str[right_pointer]:
                return False
            right_pointer -= 1

        return True


"""
The above loop actually runs approximately twice as long as it needs to. Once you pass the halfway point, you are
comparing digits that have already been checked. If we were expecting very large inputs, we could make sure to
scan only to the halfway point of the number before stopping. This would reduce the time complexity by roughly n/2,
but is probably unnecessary depending on context.

```
midpoint = int(len(x_str)/2.0)
for char in x_str[:midpoint:]:
    ...etc.
```
"""
