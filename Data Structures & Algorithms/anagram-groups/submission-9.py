class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #Mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 #a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1#z is 122, a is 97
            res[str(count)].append(s)
        return list(res.values())