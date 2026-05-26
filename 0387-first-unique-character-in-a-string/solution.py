class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = dict()

        for char in s: 
            if char in freq: 
                freq[char] = freq[char] + 1
            else: 
                freq[char] = 1
        
        for index, char in enumerate(s): 
            if freq[char] == 1: 
                return index
        return -1
