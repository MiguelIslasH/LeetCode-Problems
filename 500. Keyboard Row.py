class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {'q','w','e','r','t','y','u','i','o','p'}
        row2 = {'a','s','d','f','g','h','j','k','l'}
        row3 = {'z','x','c','v','b','n','m'}
        oneRowWords = []

        for word in words:
            if all(letter in row1 for letter in word.lower()):
                oneRowWords.append(word)
            elif all(letter in row2 for letter in word.lower()):
                oneRowWords.append(word)
            elif all(letter in row3 for letter in word.lower()):
                oneRowWords.append(word)
            
        return oneRowWords
