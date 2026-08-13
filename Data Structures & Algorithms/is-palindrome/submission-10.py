class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(s.split()) # no whitespace
        word = ""
        for i, n in enumerate(cleaned):
            if n == "." or n == "," or n == "!" or n == "?" or n == "'" or n == ";" or n == ":" :
                continue
            else:
                word += n


        word = word.lower()
        if len(word) == 1:
            return True
        elif word == word[::-1]:
            return True
        else:
            return False
            