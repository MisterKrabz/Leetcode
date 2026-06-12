class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = 0
        best = float('-inf')
        for i in nums: 
            if prev < 0: 
                prev = 0
            prev += i
            if prev > best: 
                best = prev
        
        return best

