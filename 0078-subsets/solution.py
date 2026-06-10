class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = list()
        current = list()

        def recurse(i): 
            if i == len(nums): 
                ret.append(current[:])
                return 

            recurse(i + 1)

            current.append(nums[i])
            recurse(i + 1)

            current.pop()
        
        recurse(0)
        return ret



