class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0

        frequency = dict()

        for char in secret: 
            if char in frequency: 
                frequency[char] += 1
            else: 
                frequency[char] = 1
        
        i = 0
        indicies = []
        while i < len(guess): 
            if guess[i] == secret[i]: 
                bull += 1
                frequency[guess[i]] -= 1
                indicies.append(i)
            i += 1
        i = 0
        while i < len(guess):
            if guess[i] in frequency and frequency[guess[i]] > 0 and i not in indicies: 
                cow += 1
                frequency[guess[i]] -= 1
            i += 1
        
        return str(bull) + "A" + str(cow) + "B"

