class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        
        mappings = {
            '1' : [],
            '2' : ["a", "b", "c"],
            '3' : ["d", "e", "f"],
            '4' : ["g", "h", "i"],
            '5' : ["j", "k", "l"], 
            '6' : ["m", "n", "o"], 
            '7' : ["p", "q", "r", "s"], 
            '8' : ["t", "u", "v"], 
            '9' : ["w", "x", "y", "z"], 
            '0' : [" "]
        }

        def add_numbers(digit):
            added = []
            for i in ret: 
                for j in mappings[digit]: 
                    added.append(i + j)
            return added


        ret = [""]
        for digit in digits: 
            ret = add_numbers(digit)
        
        return ret 

