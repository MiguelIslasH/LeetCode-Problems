class Solution:
    def maxPower(self, s: str) -> int:
        
        lastLetter = s[0]
        power = 1
        length = 1
        for index in range(1, len(s)):
            if s[index] == lastLetter:
                length += 1
                if length > power:
                    power = length
            else:
                if length > power:
                    power = length
                length = 1
            
            lastLetter = s[index]
        
        return power
                    
            
        
