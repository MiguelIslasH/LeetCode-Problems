class Solution:
    def toLowerCase(self, str: str) -> str:
        for index,letter in enumerate(str):
            if 64<ord(letter)<91:
                listOfString = list(str)
                listOfString[index] = chr(ord(letter)+32)
                str = "".join(listOfString)
        return str
