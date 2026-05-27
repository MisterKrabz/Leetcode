class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[0 : (len(nums))//2]
        nums2 = nums[(len(nums))//2 : len(nums)]
        ret = []
        for num in range(len(nums)//2): 
            ret.append(nums1.pop(0))
            ret.append(nums2.pop(0))

        return ret

