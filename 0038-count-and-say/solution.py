class Solution:
    def countAndSay(self, n: int) -> str:
        rle = "1"
        i = 1
        while i < n: 
            current_rle = ""
            current_char = str(rle[0])
            count = 1
            for char in rle[1:]: 
                if char == current_char: 
                    count += 1
                else: 
                    current_rle = current_rle + str(count) + str(current_char)
                    current_char = char
                    count = 1
            current_rle = current_rle + str(count) + str(current_char)
            rle = current_rle
            i += 1

        return rle 
