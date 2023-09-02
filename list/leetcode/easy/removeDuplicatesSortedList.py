#Leet code level: Easy

#Question: Remove Duplicates from sorted Array

#Breakdown:
#need to provide a non decreasing list [1,1,2,2,3,3]
#need to return the unique from it 

#Algorithm:
#step1: need to create a loop
#step2: need to find index
#step3: need to compare previous and current list and remove
#step4: return the list length
#step6: end


class Solution: 
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            if nums[i] != nums [i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    
s1 = Solution()

print(s1.removeDuplicates([1,1,2,2,3,4,5]))
print(s1.removeDuplicates([1,1,2]))
print(s1.removeDuplicates([1,1,1,1,1,1]))
print(s1.removeDuplicates([-1,0,0,0,0,3,3]))
print(s1.removeDuplicates([-1,0,0]))




