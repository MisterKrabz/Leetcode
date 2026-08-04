from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        chars = Counter(p)
        ret = []

        for i in range(len(s) - len(p) + 1): 
            current = Counter(s[i:i + len(p)])
            if current == chars: 
                ret.append(i)
        
        return ret 
