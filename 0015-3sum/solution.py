class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()

            for j in range(i + 1, len(nums)):
                needed = -nums[i] - nums[j]

                if needed in seen:
                    result.add((nums[i], needed, nums[j]))

                seen.add(nums[j])

        return [list(triplet) for triplet in result]
