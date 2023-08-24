#Leet code level: (easy)

#question: need to have a closing parenthesis 

#need to check if the stack can validate the string with parenthesis 
# first need to add string first into stack.
# and later when stack length is greater we can pop and check the element is opposite to the element or not

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == "[" or i == "{" or i == "(":
                stack.append(i)

            elif len(stack):
                pop_element = stack.pop()
                if pop_element == "(" and i != ")":
                    return False
                elif pop_element == "{" and i != "}":
                    return False
                elif pop_element == "[" and i != "]":
                    return False
            
            else:
                return False
            
        if len(stack):
            return False
        else:
            return True    
        

s1 = Solution()

print(s1.isValid("([]){})"))




