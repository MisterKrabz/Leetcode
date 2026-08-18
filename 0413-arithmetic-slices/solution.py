class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: 
            return 0

        ret = 0
        cur_slices = 0
        cur_dif = nums[1] - nums[0]
        cur_len = 2
        
        i = 2

        while i < len(nums): 
            if nums[i] - nums[i - 1] == cur_dif:
                cur_len += 1

                if cur_len >= 3: 
                    cur_slices += cur_len - 2

            else: 
                ret += cur_slices

                cur_dif = nums[i] - nums[i - 1] 
                cur_len = 2
                cur_slices = 0

            i += 1

        ret += cur_slices

        return ret
