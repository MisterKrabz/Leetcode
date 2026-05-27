class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numbers = dict()

        for i in nums: 
            if i not in numbers: 
                numbers[i] = 1
            else: 
                numbers[i] += 1
        
        sorted_keys = sorted(numbers.keys())
        ret = list()
        for i in nums: 
            total = 0
            for key in sorted_keys:
                if key >= i: 
                    break
                total += numbers[key]
            ret.append(total)
        return ret 


