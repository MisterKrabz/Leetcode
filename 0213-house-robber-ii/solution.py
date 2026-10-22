class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robHouse(hous): 
            memo = [None] * (len(hous))

            def r(houses): 
                if not houses: 
                    return 0
                if memo[len(houses) - 1] is None: 
                    memo[len(houses) - 1] = max(r(houses[0:-2]) + houses[-1], r(houses[:-1]))

                return memo[len(houses) - 1]

            return r(hous)

        return max(robHouse(nums[:-1]),  robHouse(nums[1:]))
