class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for word in words[1:]:
            cur_cnt = Counter(word)
            for char in cnt:
                cnt[char] = min(cnt[char], cur_cnt[char])
        
        res = []
        for char, cnt in cnt.items():
            res.extend(cnt * char)
        return res