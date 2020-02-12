class Solution:
    def freqAlphabets(self, s: str) -> str:
        firstLetters = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i'}
        secondLetters = {'10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z'}
        mappedString = ""
        nextStep = False
        for i, element in enumerate(s):
            if nextStep or element=='#':
                nextStep = False
                continue
            try:
                if s[i+2]=='#':
                    mappedString += secondLetters[s[i]+s[i+1]]
                    nextStep=True
            except:
                pass
            if not nextStep:
                mappedString += firstLetters[element]
        return mappedString
            
