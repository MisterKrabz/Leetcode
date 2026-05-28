class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()

        def climb(num):
            if num == 0 or num == 1:
                return 1
            elif num not in memo: 
                memo[num] = climb(num-1) + climb(num-2)
            
            return memo[num]
        
        return climb(n)
        

