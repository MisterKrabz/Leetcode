class Solution:
    def fib(self, n: int) -> int:
        memo = dict()
        memo[0] = 0
        memo[1] = 1

        def recurse(num): 
            if not (num in memo): 
                memo[num] = recurse(num - 1) + recurse(num - 2)
            return memo[num]

        return recurse(n)
