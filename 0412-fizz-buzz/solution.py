class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for num in range(1, n + 1): 
            current = ""
            if num % 3 == 0: 
                current = current + ("Fizz")
            if num % 5 == 0: 
                current = current + ("Buzz")
            
            if current == "":
                ret.append(str(num))
                continue

            ret.append(current)
        return ret 

            
