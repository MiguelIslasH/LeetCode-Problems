class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(" ")
        thirdWords = []
        if len(words) < 3:
            thirdWords
            
        for index in range(len(words)-2):
            if words[index] == first and words[index+1] == second:
                thirdWords.append(words[index+2])
            
        return thirdWords
