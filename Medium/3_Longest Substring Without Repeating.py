class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        buf=''
        stock=[]
        for char in s:
            if char not in buf:
                buf+=char
            else:
                stock+=[buf]
                if char in buf:
                    if buf.index(char)-len(stock[-1])+1 is not 0:
                        buf=stock[-1][buf.index(char)-len(stock[-1])+1:]+char
                    else:
                        buf=char
                else:
                    buf=''
        if buf is not None:
            stock+=[buf]
        return (len(max(stock, key=len)))

