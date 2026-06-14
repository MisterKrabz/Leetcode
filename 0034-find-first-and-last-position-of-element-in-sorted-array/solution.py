class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_first():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    if nums[mid] == target:
                        ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return ans

        def find_last():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    if nums[mid] == target:
                        ans = mid
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        first = find_first()

        if first == -1:
            return [-1, -1]

        last = find_last()

        return [first, last]
