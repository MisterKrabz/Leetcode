class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequencies = [0] * 200

        for char in s: 
            frequencies[ord(char)] += 1
        
        total = 0
        first = True
        for num in frequencies: 
            if num % 2 == 0: 
                total += num 
            else: 
                total += num - 1
                if first: 
                    total += 1
                    first = False

        return total 
