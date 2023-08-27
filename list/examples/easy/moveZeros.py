#Leet code level: Easy

#Question: Need to move zeroes to the last of the original list with using duplicate list

#Algorithm:
#step1: assign variable count -> 0
#step2: loop the list
#step3: check value is zero or not
#step4: swap value
#step5: increase count
#step6: end


class Solution:
    def moveZeroes(self,nums:list[int]) -> None:
        count = 0
        for index, value in enumerate(nums):
            if value != 0:
                nums[index], nums[count] = nums[count], nums[index]
                count += 1
        return nums
    
s1 = Solution()

print(s1.moveZeroes([1,0,0,2,3]))