class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        for i in range(1,n+1):
            word = ""
            if i % 3 == 0 and i % 5 != 0:
                word+="Fizz"
            elif i % 5 == 0 and i % 3 != 0:
                word+="Buzz"
            elif i % 3 == 0 and i % 5 == 0:
                word+="FizzBuzz"
            else:
                word+=str(i)
            
            answer.append(word)
            
        return answer
