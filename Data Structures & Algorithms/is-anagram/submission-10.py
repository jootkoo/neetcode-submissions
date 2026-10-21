class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}

        for x in range(len(s)):
            hashS[s[x]] = hashS.get(s[x], 0) + 1
            hashT[t[x]] = hashT.get(t[x], 0) + 1

        for key in hashS:
            if key in hashT:
                if hashS[key] == hashT[key]:
                    continue
                else:
                    return False
            else:
                return False
        return True
