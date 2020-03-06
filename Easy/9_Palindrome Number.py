class Solution:
    import math
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)

        if len(str_x)==0 or str_x[-1] is 0 or x<0:
            return False
        elif len(str_x) is 1:
            return True
        if str_x[0] is '+':
            str_x=str_x[1:]
        if len(str_x)%2 is 0:
            forward=str_x[:math.floor(len(str_x)/2)]
            back=str_x[math.floor(len(str_x)/2):][::-1]
        else:
            forward=str_x[:math.floor((len(str_x)/2))]
            back=str_x[math.floor(len(str_x)/2)+1:][::-1]
        if forward == back:
            return True
        else:
            return False
