class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = min(salary)
        maxSalary = max(salary)
        
        sumOfSalary = sum(salary) - minSalary - maxSalary
        
        return sumOfSalary/(len(salary)-2)
