class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        ret = []
        for i in nums: 
            seen.add(i)
        for i in range(len(nums)): 
            if i + 1 not in seen:
                ret.append(i + 1)
        return ret
