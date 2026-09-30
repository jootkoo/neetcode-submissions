class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": #empty
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0) #if c exists in map already, else 0

        have , need = 0 , len(countT)
        result, resLen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0) #

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need: #condition has been met
                #update result
                if (r-l+1) < resLen: #check if smaller than what is in previous
                    result = [l, r]
                    resLen = (r-l+1)
                #now shrink the window to try and get a smaller substring while conditions met
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]: #if condtions now not met
                    have -=1
                l+=1
        l, r = result
        return s[l:r+1] if resLen != float("infinity") else "" #offby one eerro 

            