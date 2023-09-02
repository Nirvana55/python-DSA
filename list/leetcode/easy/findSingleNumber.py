#leet code Level: Easy

#Question: Need to find the single Number

#Breakdown:
#Best answer:
#Xor of any two num gives the difference of bit as 1 and same bit as 0.
#Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
#So, we will always get the single element because all the same ones will evaluate to 0 and 0^single_number = single_number.

#Algorithm:
#step1: variable xor -> 0
#step2: loop 
#step3: set bit of num 
#step4: return the bit with 1

class Solution:
    def findSingleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor
    
s1 = Solution()
print(s1.findSingleNumber([2,2,1,1,3]))