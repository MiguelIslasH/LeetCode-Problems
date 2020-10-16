class Solution:
    def findMinimumDiff(self, arr):
        #-5, -3, 0, 2
        minimumDiff = abs(arr[0] - arr[1]) # 3
        for iterator in range(1, len(arr)-1): #it = 2
            diff = abs(arr[iterator] - arr[iterator+1]) #2
            if(diff<minimumDiff):
                minimumDiff = diff
        return minimumDiff #2
    
    def findMinimumPairs(self, arr, minimumDiff):
        pairs = []
        #-5, -3, 0, 2
        #mindiff = 2
        for iterator in range(0, len(arr)-1):
            diff = abs(arr[iterator] - arr[iterator+1]) #2
            if diff == minimumDiff: #true
                pairs.append([arr[iterator], arr[iterator+1]])
        
        return pairs
        
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        #-4,-5,3,-2,1
        #(0...n-2)
        #-5,-4,-2,1,3
        #abs(arr[i]-arr[i+1])
        #1
        #[[1,2], [2,3], [3,4]]
        #Time: O(nlogn + n + n) = O(nlogn)
        #Space: O(n)
        
        #-3, -5, 0, 2
        arr.sort()
        #-5, -3, 0 ,2
        if len(arr)==2:
            return [[arr[0], arr[1]]]
        
        minimumDiff = self.findMinimumDiff(arr)
        return self.findMinimumPairs(arr, minimumDiff)
