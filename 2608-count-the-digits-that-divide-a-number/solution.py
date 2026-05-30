class Solution:
    def countDigits(self, num: int) -> int:
        ret = 0
        orig = num
        while num: 
            if orig % (num % 10) == 0: 
                ret += 1
            num = num // 10
        return ret 
        
        
