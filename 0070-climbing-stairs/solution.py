class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()

        def climb(n): 
            if n == 0: 
                return 1
            elif n == 1: 
                return 1
            elif n in memo: 
                return memo[n]
            else: 
                memo[n] = climb(n-1) + climb(n-2)
                return memo[n]

        return climb(n)
