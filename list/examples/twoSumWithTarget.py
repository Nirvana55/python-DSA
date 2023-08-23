#Leet code Level: (Easy)

#Question is to find the index of the list where matches the total of the target

#Breakdown:
#need to loop through list to find the index 
#to find the index and the sum of the target we used enumerate loop
#enumerate loop gives us count and variable
#after that subtracted the value to find the number 
#if the number is seen than we put the value of calculation in the array and the count of the next variable
#else we append
#end

class Solution:
    def twoSum(self,nums:list[int],target:int):
        seen = {}
        for count,value in enumerate(nums):
            calculation = target - nums[count]
            if calculation in seen:
               return [seen[calculation],count]  
            seen[value] = count

s1 = Solution()
print(s1.twoSum([2,7,10,11],9))
print(s1.twoSum([3,3],6))

