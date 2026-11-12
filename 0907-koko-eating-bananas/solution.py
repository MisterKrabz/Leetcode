class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def time_needed(speed): 
            hours = 0
            nonlocal piles 
            for bananas in piles: 
                hours += math.ceil(bananas / speed)
            return hours 
        
        if len(piles) > h: 
            return -1 

        piles.sort()
        left = 1
        right = piles[-1]
        while left < right: 
            mid = (left + right) // 2
            hours = time_needed(mid)

            # too slow, need to increase speed 
            if hours > h: 
                left = mid + 1
                prev_mid = mid 
                continue 
            # fast enough, see if a slower speed can suffice 
            else: 
                right = mid 

        return left 
            
