class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = list(range(1,len(arr)+k+1))
        dif = list(set(missing) - set(arr))
        dif.sort()
        return dif[k-1]
