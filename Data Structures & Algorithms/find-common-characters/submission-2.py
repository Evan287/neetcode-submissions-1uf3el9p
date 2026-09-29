class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])

        for word in words[1:]:
            cur_cnt = Counter(word)
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])
        
        res = []
        for c, count in cnt.items():
            res.extend(c * count)

        return res