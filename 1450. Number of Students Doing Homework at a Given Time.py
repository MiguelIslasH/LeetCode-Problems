class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        numberOfStudents = 0
    
        for index in range(len(startTime)):
            if startTime[index] <= queryTime <= endTime[index]:
                numberOfStudents += 1
        
        return numberOfStudents
