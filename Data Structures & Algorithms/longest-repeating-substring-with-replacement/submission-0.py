class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashm = {}
        total = 0

        for i in range(len(s)):
            if s[i] not in hashm:
                hashm[s[i]] = 1
            else:
                hashm[s[i]] += 1

            windowSize = (i - l + 1) - max(hashm.values()) #tells us the replacements
            while windowSize > k:
                hashm[s[l]] -=1
                l+= 1
                windowSize = (i - l + 1) - max(hashm.values())

            total = max(total, i - l + 1)
        return total

            
                
