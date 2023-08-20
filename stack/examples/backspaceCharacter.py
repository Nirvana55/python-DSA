#Leet code level: (easy)

#question: to backspace if contains "#" and compare text

#step1: loop the two string
#step2: check if they contain # 
#step3: if they contain # pop else append
#step4: compare both string and check they are same or not

class Solution:
    def backspaceCompare(self,s:str,t:str) -> bool:
        a = self.checkLoop(s)
        b = self.checkLoop(t)
        return a == b

    def checkLoop(self,s:str) -> list:
        stack = []
        for i in s:
            if i != "#":
                stack.append(i)
            elif len(stack):
                stack.pop()
        return stack
      
          
s1 = Solution()

print(s1.backspaceCompare("a#","a#"))
print(s1.backspaceCompare("ab#","ac##"))