class Solution:
    def addDigits(self, num: int) -> int:
        number = num
        while True: 
            digits = []
            while number != 0: 
                digits.append(number % 10)
                number = number // 10
            if sum(digits) // 10 == 0: 
                return sum(digits)
            else: 
                number = sum(digits)
            
        
        
