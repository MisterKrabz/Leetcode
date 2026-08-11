class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ret = set()

        for i in range(len(nums)): 
            for j in range(i + 1, len(nums)): 
                p1 = j + 1
                p2 = len(nums) - 1
                goal = target - nums[i] - nums[j]

                while p1 < p2: 
                    if nums[p1] + nums[p2] == goal: 
                        ret.add((nums[i], nums[j], nums[p1], nums[p2]))
                        p2 -= 1
                        p1 += 1
                    elif nums[p1] + nums[p2] > goal: 
                        p2 -= 1
                    else: 
                        p1 += 1

        ret = list(ret)
        for val in ret: 
            val = list(val)

        return ret 
