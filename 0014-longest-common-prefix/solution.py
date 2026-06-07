class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(min(strs, key=len))):
            char = strs[0][i]

            for j in range(len(strs)):
                if strs[j][i] != char:
                    return strs[0][:i]

        return min(strs, key=len)
