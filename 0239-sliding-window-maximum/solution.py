from collections import Counter

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums[0:k])
        current_max = max(freq)
        ret = [current_max]

        i = k
        while i < len(nums): 
            current_max = max(nums[i], current_max)

            freq[nums[i]] += 1
            freq[nums[i-k]] -= 1
            if freq[current_max] == 0: 
                current_max = max(nums[i-k+1:i+1])
            
            ret.append(current_max)

            i += 1

        return ret 
