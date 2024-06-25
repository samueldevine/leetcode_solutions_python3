class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numeral_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        prev_value = 0
        for char in s:
            current_value = roman_numeral_values[char]
            if current_value > prev_value:
                result += current_value - (2 * prev_value)
            else:
                result += current_value

            prev_value = current_value
        return result


"""
Process:
Loop through each char in the string. keep track of the previous value.
    Values should generally be in descending order, so...
    - If the current value is indeed lower than the previous value, we can
      simply add it to the running sum and move on
    - If the current value is HIGHER than the previous value however, this is a
      special subtraction case (i.e. IV = 4, not 6). Since in this example we
      have already incorrectly added 1 to the total instead of subtracting it,
      we can subtract it twice
    Set previous value to current value before next loop

O(n) time: we need to loop through the entire string once
O(1) memory: we are using a constant dict for the values and a constant number of variables
"""
