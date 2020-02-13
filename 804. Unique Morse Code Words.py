class Solution:
    def getMorseCode(self, word:str)->str:
        morseMappedWord = ""
        for letter in word:
            morseMappedWord+=self.morseCode[ord(letter)-97]
        return morseMappedWord
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        self.morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        uniqueMorseWords = set()
        for word in words:
            mappedWord = self.getMorseCode(word) 
            if mappedWord not in uniqueMorseWords:
                uniqueMorseWords.add(mappedWord)
        return len(uniqueMorseWords)
