class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Found target
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted (safe)
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    # Target is in the sorted left half
                    right = mid - 1
                else:
                    # Target is in the right half (may have rotation)
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    # Target is in the sorted right half
                    left = mid + 1
                else:
                    # Target is in the left half (may have rotation)
                    right = mid - 1
        
        return -1  # Target not found

