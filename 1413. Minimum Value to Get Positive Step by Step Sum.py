class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for num in range(1, 10001):
            suma = num
            flag = True
            for i in nums:
                suma += i
                if suma < 1:
                    flag = False
                    break
            if flag == True:
                return num
