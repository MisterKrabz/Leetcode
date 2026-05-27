class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = ""
        for i in range(min(len(word1), len(word2))): 
            ret = ret + word1[i]
            ret = ret + word2[i]
        
        ret = ret + word1[min(len(word1), len(word2)): len(word1)]
        ret = ret + word2[min(len(word1), len(word2)): len(word2)]

        return ret
