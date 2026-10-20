class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        res = []
        for s in strs:
            sortedS = "".join(sorted(s))
            anagrams[sortedS].append(s)

        for anagram in anagrams.values():
            res.extend([anagram])
        return res