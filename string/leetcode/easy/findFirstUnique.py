#leet code level: Easy

#Question: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

#algorithm:
#count the value of s
# check the value of count and return value with 1
#end
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        new_list = Counter(s)
        for i in range(len(s)):
            if new_list[s[i]] == 1:
                return i
        return -1
    
s1 = Solution()
print(s1.firstUniqChar("leetcode"))


