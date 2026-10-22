class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]

        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])

        sums = {}
        count = 0

        for num in prefix_sum:
            target = num - k

            count += sums.get(target, 0)

            sums[num] = sums.get(num, 0) + 1

        return count
