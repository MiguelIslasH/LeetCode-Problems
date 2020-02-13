class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        newMatrix = [None for _ in range(len(A))]
        for index, individualList in enumerate(A):
            individualList.reverse()
            for number in individualList:
                if newMatrix[index] == None:
                        newMatrix[index] = list()
                if number == 0:
                    newMatrix[index].append(1)
                else:
                    newMatrix[index].append(0)
        return newMatrix
                
