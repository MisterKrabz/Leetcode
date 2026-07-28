class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        
        for num in nums: 
            index = abs(num) - 1

            if nums[index] < 0: 
                ret.append(abs(num))
            
            nums[index] = 0 - nums[index]

        return ret
