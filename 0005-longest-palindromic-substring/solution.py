class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        window_length = len(s)
        while window_length > 0: 
            start = 0
            while start + window_length <= len(s): 
                end = start + window_length
                sub = s[start:end]
                if sub == sub[::-1]:
                    return s[start:end]
                start += 1

            window_length = window_length - 1
