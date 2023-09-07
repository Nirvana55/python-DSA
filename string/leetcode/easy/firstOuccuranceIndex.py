#leet code level :Easy

#question: need to find the index of the given string

#these are easy solution so no breakdown

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
           return haystack.index(needle)
        else:
            return -1
        
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif needle not in haystack:
            return -1
        else:
            return len(haystack.split(needle)[0])


s1 = Solution()
s2 = Solution2()
s3 = Solution3()


print(s1.strStr("sadbutsad", "sad"))
print(s2.strStr("sadbutsad", "sad"))
print(s3.strStr("sadbutsad", "sad"))