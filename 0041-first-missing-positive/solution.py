class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        i = 1
        for num in nums: 
            if i > num: 
                continue 
            if i < num: 
                return i
            i += 1
        return max(1, nums[-1] + 1)
            
