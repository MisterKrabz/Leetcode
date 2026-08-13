from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
            
        def split(start, end): 
            if end - start + 1 < k:
                return 0
                
            frequencies = Counter(s[start:end+1])
            
            valid = True
            for char in frequencies: 
                if frequencies[char] < k: 
                    valid = False
                    break
            
            if valid: 
                return end - start + 1

            max_len = 0
            segment_start = start
            
            for i in range(start, end + 1): 
                if frequencies[s[i]] < k: 
                    if i > segment_start:
                        max_len = max(max_len, split(segment_start, i - 1))
                    segment_start = i + 1

            if segment_start <= end:
                max_len = max(max_len, split(segment_start, end))
                
            return max_len
        
        return split(0, len(s) - 1)

