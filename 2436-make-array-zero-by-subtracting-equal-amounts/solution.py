class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        seen.add(0)
        distinct = 0

        for element in nums: 
            if element not in seen: 
                distinct += 1
                seen.add(element)
        
        return distinct

        


