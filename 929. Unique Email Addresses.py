class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        newEmail = ""
        emailsCounter = {}
        foundPlus = True
        foundAt = False
        for email in emails:
            newEmail = ""
            foundPlus = True
            foundAt = False
            for letter in email:
                if letter == '+':
                    foundPlus = False
                    
                if letter == '@':
                    foundPlus = True
                    foundAt = True
                    
                if foundPlus:
                    if letter=='.' and foundAt == False:
                        pass
                    else:
                        newEmail+=letter
                        
            if emailsCounter.get(newEmail) == None:
                emailsCounter[newEmail] = 1
            else:
                emailsCounter[newEmail] += 1
        return len(emailsCounter)
