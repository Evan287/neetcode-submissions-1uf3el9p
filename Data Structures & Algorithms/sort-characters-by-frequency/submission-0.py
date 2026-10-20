class Solution:
    def frequencySort(self, s: str) -> str:
        #frequency -> hashmap
        #return the characters that appear most first
        #to return extend and multiply by the count 
        count = Counter(s)
        buckets = defaultdict(list)

        for char, freq in count.items():
            buckets[freq].append(char)
        
        res = []
        for i in range(len(s), 0, -1):
            if i in buckets:
                for c in buckets[i]:
                    res.append(c * i)
        return "".join(res)