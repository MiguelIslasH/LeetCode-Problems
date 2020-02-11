class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        setOfJewls = set([value for value in J])
        jewels=0
        for stone in S:
            if stone in setOfJewls:
                jewels+=1
        return jewels
