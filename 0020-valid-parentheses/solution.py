class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: 
            return False
        stack = list()
        for char in s: 
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else: 
                if len(stack) == 0: 
                    return False
                char1 = stack.pop(-1)

                if char1 == "(" and char == ")":
                    continue
                if char1 == "[" and char == "]":
                    continue
                if char1 == "{" and char == "}":
                    continue 
                return False
            
        if len(stack) != 0: 
            return False
            
        return True
            

