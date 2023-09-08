#leet code level: Easy

#Question: need to find the anagram of two strings

#Breakdown:
#we can sort two string 
#we can loop the two string sort them and fix them 
from collections import Counter

class Solution:
    def isAnagram(self,s:str,t:str) -> bool:
        c = Counter(s)
        d = Counter(t)

        return c == d
    
class Solution:
    def isAnagram(self,s:str,t:str) -> bool:
        c = sorted(s)
        d = sorted(t)
        
        return c == d
        
    
s1 = Solution()
s2 = Solution()

print(s1.isAnagram("anagram","sad"))
print(s2.isAnagram("anagram","sad"))