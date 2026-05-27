class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        indexes = [0] * (len(nums))
        loss = 0
        rep = 0
        
        for i, num in enumerate(nums): 
            indexes[num - 1] += 1
        for i in range(len(indexes)): 
            if indexes[i] == 2: 
                rep = i + 1
            if indexes[i] == 0: 
                loss = i + 1
        
        return [rep, loss]
            
        

        


            
        

