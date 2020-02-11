class Solution:
    def defangIPaddr(self, address: str) -> str:
        for index, element in enumerate(address):
            if element=='.':
                listOfString = list(address)
                listOfString[index] = '[.]'
                address = "".join(listOfString)
        return address
