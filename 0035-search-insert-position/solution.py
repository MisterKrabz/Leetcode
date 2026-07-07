class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]: 
            return 0

        i = 0
        while i < len(nums): 
            if nums[i] == target: 
                return i 

            if i + 1 < len(nums) and  nums[i] < target and nums[i+1] > target: 
                return i + 1

            i += 1
        
        return len(nums)
