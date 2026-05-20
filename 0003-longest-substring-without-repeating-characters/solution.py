class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0

        for i in range(len(s)): 
            current_index = i
            current_used = set()
            while current_index < len(s) and s[current_index] not in current_used: 
                current_used.add(s[current_index])
                current_index += 1

            if len(current_used) > max_length: 
                max_length = len(current_used)
        return max_length
        
