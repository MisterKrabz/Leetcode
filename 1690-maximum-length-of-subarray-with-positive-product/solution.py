class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        best = 0
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == 0:
                i += 1
                continue

            start = i
            negatives = 0
            first_negative = -1
            last_negative = -1

            while i < n and nums[i] != 0:
                if nums[i] < 0:
                    negatives += 1

                    if first_negative == -1:
                        first_negative = i

                    last_negative = i

                i += 1

            length = i - start

            if length <= best:
                continue

            if negatives % 2 == 0:
                best = length
            else:
                remove_prefix = i - first_negative - 1

                remove_suffix = last_negative - start

                best = max(best, remove_prefix, remove_suffix)

        return best
