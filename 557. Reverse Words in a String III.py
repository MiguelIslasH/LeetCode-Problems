class Solution:
    def reverseWords(self, s: str) -> str:
        reversedString = ""
        reversedWord = ""
        words = s.split(" ")
        for index, word in enumerate(words):
            for letter in reversed(word):
                reversedString += letter
            if index < len(words)-1:
                reversedString += " " 
        return reversedString
