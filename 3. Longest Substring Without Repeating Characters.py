class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenghtOfLS = 0
        collection=set()
        
        for index in range(len(s)):
            newString=s[index:]
            for letter in newString:
                if letter in collection:
                        break
                else:
                    collection.add(letter)
                if len(collection) > lenghtOfLS:
                    lenghtOfLS = len(collection)
            collection=set()
        return lenghtOfLS
