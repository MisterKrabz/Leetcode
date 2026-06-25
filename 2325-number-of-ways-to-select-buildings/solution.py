from collections import Counter 
class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = s.count('0')
        ones = len(s) - zeros

        zeros_left = 0
        ones_left = 0

        total = 0

        for char in s: 
            if char == '0': 
                total += ones_left * (ones - ones_left)
                zeros_left += 1
            else: 
                total += zeros_left * (zeros - zeros_left)
                ones_left += 1
        
        return total
