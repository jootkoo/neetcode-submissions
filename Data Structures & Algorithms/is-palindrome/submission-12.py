class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(s.split()).lower()
        punc = {"!", ".", "?", "'", ";", ":","," }
        word = ""

        for char in clean:
            if char in punc:
                continue
            word += char
    
        if word == word[::-1]:
            return True
        return False

            