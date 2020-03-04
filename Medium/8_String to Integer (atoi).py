class Solution:
    def myAtoi(self, str: str) -> int:
        minus=False
        while len(str)>0 and str[0] is ' ':
            str=str[1:]
        if len(str)>0:
            if str[0] is '-':
                str=str[1:]
                minus=True
            elif str[0] is '+':
                str=str[1:]
        num_str=''
        for i in range(len(str)):
            if str[i].isdecimal():
                num_str+=str[i]
            else:
                if len(str)>i+2 and str[i+1] is '.' and str[i+2].isdecimal():
                    num_str='0'
                break
        if num_str is '':
            num_str='0'
        if minus:
            num_str='-'+num_str
        num=int(num_str)
        if num>2147483647:
            num=2147483647
        if num<-2147483648:
            num=-2147483648            
        return num