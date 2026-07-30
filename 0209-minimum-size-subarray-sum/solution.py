class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ret = len(nums) + 1
        left = 0
        current_sum = 0 
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= target:
                ret = min(ret, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return 0 if ret == len(nums) + 1 else ret
