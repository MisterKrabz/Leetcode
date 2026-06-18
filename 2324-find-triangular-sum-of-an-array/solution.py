class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        while nums: 
            if len(nums) == 2: 
                return (nums[0] + nums[1]) % 10
            else: 
                result = []
                i = 1
                while i < len(nums): 
                    result.append((nums[i] + nums[i-1]) % 10)
                    i += 1
                
                nums = result 
    
