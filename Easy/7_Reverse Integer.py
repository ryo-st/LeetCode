class Solution:
    def reverse(self, x: int) -> int:
        val=str(x)[::-1]
        if val[-1] is '-':
            val='-'+val[:-1]
        if int(val)>2147483647 or int(val)<-2147483648:
            val=0
        return int(val)