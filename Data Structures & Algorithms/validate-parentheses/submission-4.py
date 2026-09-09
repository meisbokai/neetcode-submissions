class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False
        
        if len(s)%2==1:
            return False

        opening = {'{', '[', '('}
        closing = {'}', ']', ')'}
        closer = {
            "}" : "{" ,
            "]" : "[" ,
            ")" : "(" 
        }
        
        
        stack = []

        for i in range( len(s)):
            print(stack)
            if s[i] in opening:
                stack.append(s[i])
            elif s[i] in closing:
                if len(stack) == 0:
                    return False
                if stack[-1] == closer[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack) == 0
            
        