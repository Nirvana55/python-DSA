#leet code level: easy

#Question: need to find the intersection between two list

#breakdown:
#we created two pointers
#i and j
#created a loop
#if first_list equal we append
#else if first is smaller than second we add i
#else we add j
#sorting is necessary due to it
#end

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection_list = [] 
        first_list = sorted(nums1) 
        second_list = sorted(nums2) 
        i, j = 0, 0
        while i < len(first_list) and j < len(second_list):
            if first_list[i] == second_list[j]:
                intersection_list.append(first_list[i])
                i += 1
                j += 1
            elif first_list[i] < second_list[j]:
                i += 1
            else:
                j += 1
        
        return intersection_list
    
s1 = Solution()
print(s1.intersect([1,2,2,1], [2,2]))
print(s1.intersect([1,2,2,1], [1,2]))
print(s1.intersect([1,2,2,1], [2]))
print(s1.intersect([4,9,5], [9,4,9,8,4]))