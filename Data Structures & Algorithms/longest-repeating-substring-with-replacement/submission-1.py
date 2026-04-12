class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        l = 0
        count = {}
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            sub_length = r - l + 1
            
            if sub_length - max_freq > k:
                count[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
        return length
