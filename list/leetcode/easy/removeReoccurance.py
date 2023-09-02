#Leet code Level: Easy

#Question: Need to have a list, need to remove duplicate which is equal to target integer from the list

#Breakdown: Algorithm
#need to loop
#need to check if the target is equal to the iterator in the loop
#and if it does remove the element

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in nums[:]:
            if i == val:
                nums.remove(i)
        return len(nums)
    
s1=Solution()

print(s1.removeElement([3,2,2,3],3))
print(s1.removeElement([0,1,2,2,3,0,4,2],2))