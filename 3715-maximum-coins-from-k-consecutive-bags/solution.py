
class Solution:
    def maximumCoins(self, coins: list[list[int]], k: int) -> int:
        coins.sort()
        n = len(coins)
        prefix = [0]

        for l, r, c in coins:
            total = (r - l + 1) * c
            prefix.append(prefix[-1] + total)

        def coins_through(x):
            left = 0
            right = n

            while left < right:
                mid = (left + right) // 2

                if coins[mid][0] <= x:
                    left = mid + 1
                else:
                    right = mid

            i = left - 1

            if i < 0:
                return 0

            l, r, c = coins[i]

            return prefix[i] + (min(x, r) - l + 1) * c

        def window_sum(start):
            end = start + k - 1
            return coins_through(end) - coins_through(start - 1)

        answer = 0

        for l, r, c in coins:
            answer = max(answer, window_sum(l))
            answer = max(answer, window_sum(r - k + 1))

        return answer

