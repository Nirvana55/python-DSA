#Leet code level: (medium)

#question: to simplify the path 
# objective is to ignore multiple "/" and if has ".." or "." pop and show remaining text

#step1: we can split the text "/"
#step2: we can loop 
#step3: we can check the objective condition 
#step4: join the split text by "/"
#step4: return text

class Solution:
    def simplifyPath(self,path:str) -> str:
        stack = []
        split_str = path.split("/")

        for character in split_str:
            if character == "..":
                if stack:
                    stack.pop()
            elif character and character != ".":
                stack.append(character)
        
        return "/"+"/".join(stack)
    
s1 = Solution()
print(s1.simplifyPath("///a/b/ssd////..////../asd/"))
print(s1.simplifyPath("/a/./b/../../c/"))
print(s1.simplifyPath(""))







