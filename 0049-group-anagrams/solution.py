class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for string in strs: 
            base = sorted(string)
            base = "".join(base)
            
            if base in anagrams: 
                anagrams[base].append(string)
            else: 
                anagrams[base] = [string]
        
        return list(anagrams.values())


