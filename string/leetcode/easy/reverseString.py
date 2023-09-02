#Leet code level: Easy

#Write a function that reverses a string. The input string is given as an array of characters s.

#Algorithm:
#step1:need to loop the value with range and start from the right side by slice
#step2: need to overwrite the value 
#step3: return the value

#time complexity 0(n) space complexity 0(1)
class Solution:
   def reverseString(self, s:list[str])-> list[str]:
        for i, value in enumerate(s[::-1]):
            s[i] = value
        return s

s1 = Solution()
print(s1.reverseString(["h","e","l","l","o"]))