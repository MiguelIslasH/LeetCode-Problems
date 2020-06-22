class Solution:
    def balancedStringSplit(self, s: str) -> int:
        LCounter = 0
        RCounter = 0
        maxNumberOfBalancedStrings = 0
        
        for letter in s:
            if letter == "L":
                LCounter += 1
            else:
                RCounter += 1
            
            if LCounter == RCounter:
                maxNumberOfBalancedStrings += 1
        
        return maxNumberOfBalancedStrings
