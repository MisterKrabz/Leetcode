class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = set()
        ret = set()
        
        for start in range(len(s) - 9): 
            if s[start:start + 10] in sequences: 
                ret.add(s[start:start + 10])
            else: 
                sequences.add(s[start:start + 10])
        return list(ret)
