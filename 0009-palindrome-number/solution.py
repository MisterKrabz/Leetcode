class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False

        digits = list()

        while x != 0: 
            digits.append(x % 10)
            x = x // 10
        
        while len(digits) >= 2: 
            if digits.pop(0) != digits.pop(-1): 
                return False
        return True


            
