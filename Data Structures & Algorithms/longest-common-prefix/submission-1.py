class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key=len)
        #Start with the smallest word
        for index, char in enumerate(prefix):
            for string in strs:
                if string[index] != char:
                    return prefix[:index]
        return prefix
