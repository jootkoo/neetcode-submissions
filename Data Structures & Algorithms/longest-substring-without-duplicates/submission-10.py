class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        longest = 0
        for i, n in enumerate(s):
            while n in seen:
                seen.remove(s[l])
                l +=1

            seen.add(n)
            longest = max(longest, i - l + 1)
        return longest