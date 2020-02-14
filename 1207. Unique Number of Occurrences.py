class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numberOfOcurrences={}
        for element in arr:
            if numberOfOcurrences.get(element) != None:
                numberOfOcurrences[element]+=1
            else:
                numberOfOcurrences[element] = 0
        uniqueNumberOfOcurrences= set()
        for number in numberOfOcurrences:
            if numberOfOcurrences[number] in uniqueNumberOfOcurrences:
                return False
            else:
                uniqueNumberOfOcurrences.add(numberOfOcurrences[number])
        return True
