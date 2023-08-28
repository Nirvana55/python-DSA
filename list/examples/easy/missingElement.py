#leet code level: Easy

#Question: need to find the missing element from the list from the range

#choose the best solution

# this was the solution 1 its time complexity is 0(n) but space complexity is 0(n) so it was bad in response
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        value = []
        for i in range(len(nums) + 1):
            value.append(i)

        difference = list(set(value) - set(nums))
        return difference[0]
    
#Here we are using bit manipulation:
#when we do xor if the number is not same it returns 1 else false
#when we do it we are comparing list containing all range and normal list
#since bit are commutative they try to cancel each other
#so difference is font this way

# here time complexity is 0(n) and space complexity is 0(1)
class Solution2:
    def missingNumber(self, nums: list[int]) -> int:
        value = 0
        for i in range(len(nums)+1):
            value ^= i

        for i in nums:
            value ^= i
        
        return value
    
#Here we are using formula to calculate the range 

# here time complexity is 0(1) and space complexity is 0(1)
class Solution3:
    def missingNumber(self,nums: list[int]) -> int:
        n = len(nums)
        total = ((n * (n+1))) //2

        actual = sum(nums)
        difference = total - actual
        return difference

s1 = Solution()
s2 = Solution2()
s3 = Solution3()

print(s1.missingNumber([3,0,1]),"s1")
print(s1.missingNumber([0,1]),"s1")
print(s1.missingNumber([9,6,4,2,3,5,7,0,1]),"s1")

print(s2.missingNumber([3,0,1]),"s2")
print(s2.missingNumber([0,1]),"s2")
print(s2.missingNumber([9,6,4,2,3,5,7,0,1]),"s2")

print(s3.missingNumber([3,0,1]),"s3")
print(s3.missingNumber([0,1]),"s3")
print(s3.missingNumber([9,6,4,2,3,5,7,0,1]),"s3")