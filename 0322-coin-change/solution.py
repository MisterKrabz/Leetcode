class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # amount : fewest number of coins 
        memo = {0:0}
        for coin in coins: 
            memo[coin] = 1

        def recurse(amount): 
            options = []
            if amount in memo: 
                return memo[amount]
            for coin in coins: 
                if amount - coin >= 0: 
                    result = recurse(amount - coin) 
                    if result != -1: 
                        options.append(result + 1)
            if not options: 
                memo[amount] = -1
                return -1
            memo[amount] = min(options)
            return memo[amount]

        
        if recurse(amount) >= 0: 
            return recurse(amount)
        return -1 

            

