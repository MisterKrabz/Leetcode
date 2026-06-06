class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        esum = 0
        dsum = 0
        
        for num in nums: 
            esum += num

            while num != 0: 
                dsum += num % 10
                num = num // 10
            
        return abs(esum - dsum)
