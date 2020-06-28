class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target)==0 and len(arr)==0:
            return True
    
        targetMap = {}
        arrMap = {}
        
        for number in target:
            if not targetMap.get(number):
                targetMap[number] = 1
            else:
                targetMap[number] += 1
        
        for number in arr:
            if not arrMap.get(number):
                arrMap[number] = 1
            else:
                arrMap[number] += 1
                
        for key in targetMap:
            if not arrMap.get(key):
                return False
            else:
                if targetMap[key] != arrMap[key]:
                    return False
        return True
