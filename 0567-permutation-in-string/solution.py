from collections import Counter 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequencies = Counter(s1)

        left = 0
        right = 0
        current_frequencies = dict()
        current_length = 0

        while right < len(s2): 
            if current_length == len(s1): 
                return True

            if s2[right] not in frequencies: 
                current_frequencies = dict()
                current_length = 0
                right += 1
                left = right 
                continue 

            current_frequencies[s2[right]] = current_frequencies.get(s2[right], 0) + 1

            while current_frequencies[s2[right]] > frequencies[s2[right]]: 
                current_frequencies[s2[left]] -= 1
                left += 1
                current_length -= 1
            
            right += 1
            current_length += 1

        if current_length == len(s1): 
            return True
        return False 
