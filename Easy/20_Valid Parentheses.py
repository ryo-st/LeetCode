class Solution:
    def isValid(self, s: str) -> bool:
        brackets=""
        for char in s:
            if char is "(" or char is "{" or char is "[":
                brackets+=char
            elif char is ")" and len(brackets)>0 and brackets[-1] is "(":
                brackets=brackets[:-1]
            elif char is "}" and len(brackets)>0 and brackets[-1] is "{":
                brackets=brackets[:-1]
            elif char is "]" and len(brackets)>0 and brackets[-1] is "[":
                brackets=brackets[:-1]
            else:
                return False
            
        if len(brackets) is 0:
            return True
        else:
            return False