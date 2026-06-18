class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        shift = 0
        i = 0
        while i < len(nums): 
            if nums[i] == val: 
                shift += 1

            else: 
                nums[i - shift] =  nums[i]
            i += 1
            
        return len(nums) - shift
            
                
