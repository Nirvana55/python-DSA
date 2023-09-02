#Leet code level: Easy

#Question: need to return true or false if the list contain a duplicate value

#Algorithm1:
#step1: need to loop the entire list
#step2: need to check if the list contain the prev value
#step3: if has the value return true 
#step4: else false
#step5: end

#Algorithm2:
#step1: assign variable seen -> Set()
#step2: need to loop the entire list
#step3: need to check if the list contain the value
#step4: if has the value return true 
#step5: add value to set
#step6: return False
#step7: end

# This is also one approach but in leet code it exceeds the time limit when having large list 
# cause this have time complexity of O(n^2)
class Solution:
    def containDuplicate(self,nums:list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

# This might be other solution this will time complexity of o(n)
class Solution2:
    def containsDuplicate(self, nums:list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

s1 = Solution()
s2 = Solution2()

print(s1.containDuplicate([1,2,3,4]))
print(s1.containDuplicate([1,2,3,4,3]))
print(s2.containsDuplicate([1,2,3,4]))
print(s2.containsDuplicate([1,2,3,4,4]))