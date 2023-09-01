#leet code level: Easy

#Question: need to check if the string is a valid palindrome or not

#Algorithm:
#step1: need to remove the non-alphabetical letters and make all same
#step3: reverse the given string and assign in a variable
#step4: compare if valid return true 
#step5: else false

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        return s == s[::-1]
    

#Algorithm:
#step1: created two pointers 
#step3: loop until i is less than j
#step4: if both are is non alpha numeric we add i and subtract j to check next
#step5: if not equal we return false
#step6: continue the loop
#step7: if not alpha numeric we add i with 1 and j with - 1 (True == +1) 
#step8: if loop ends we return true
#step9: end

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b: return False
                else:
                    i, j = i + 1, j - 1
                    continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True


s1 = Solution1()
s2 = Solution2()

print(s1.isPalindrome("A man, a plan, a canal: Panama"))
print(s1.isPalindrome("0P"))

print(s2.isPalindrome("A man, a plan, a canal: Panama"))
print(s2.isPalindrome("0P"))
