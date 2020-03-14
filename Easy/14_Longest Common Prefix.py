class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        prefix=strs[0]
        for l in strs[1:]:
            if len(prefix)==0:
                return ""
            if len(prefix)<len(l):
                l=l[:len(prefix)]
            elif len(prefix)>len(l):
                prefix=prefix[:len(l)]
            c_prefix=prefix
            while not(l == c_prefix):                
                if len(l)==0:
                    return ""
                l=l[:-1]
                c_prefix=c_prefix[:-1]
            prefix=l
        return prefix