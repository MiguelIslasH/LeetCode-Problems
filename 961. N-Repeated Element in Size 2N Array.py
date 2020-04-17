class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        numberOfTimesInArray=set()
        for number in A:
            if number in numberOfTimesInArray:
                return number
            else:
                numberOfTimesInArray.add(number)
