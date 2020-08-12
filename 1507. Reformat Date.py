class Solution:
    def reformatDate(self, date: str) -> str:
        components = date.split(" ")
        day = None
        month = None
        year = None
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        if len(components[0]) == 3:
            day = "0"+str(components[0][0])    
        else:
            day = str(components[0][0])+str(components[0][1])
        
        numberMonth = (months.index(components[1]))+1
        if len(str(numberMonth))==1:
            month = "0"+str(numberMonth)
        else:
            month = str(numberMonth)
        
        return (components[2]+"-"+str(month)+"-"+day)
