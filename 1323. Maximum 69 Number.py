class Solution:
    def maximum69Number (self, num: int) -> int:
        number = str(num)
        for i,element in enumerate(number):
            if element == '6':
                lista = [x for x in str(num)]
                lista[i]='9'
                print("".join(lista))
                return "".join(lista)
        return num
