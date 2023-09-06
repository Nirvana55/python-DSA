#leet code level: Easy

#Question: Merge Sorted Array

#Breakdown
#need to create pointers with value 0
#need to create a copy list of num1 to initialize the value
#need to check the length of the list
#need to check the element value and add to num1 and increase the pointers value according to it
#when the length reaches the loop exit 
#need to check the remaining value of the list on nums1 and nums2
#need to add if the value is less than the length
#return value of num1

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1, p2, p = 0,0,0
        copy_num1 = nums1[::]

        while p1 < m and p2 < n:
            if copy_num1[p1] < nums2[p2]:
                nums1[p] = copy_num1[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1

        while p2 < n:
            nums1[p] = nums2[p2]
            p2 += 1
            p += 1

        while p1 < m:
            nums1[p] = copy_num1[p1]
            p1 += 1
            p += 1
            
        return nums1
    
    
class Solution2:
     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        add_list = nums1[:m] + nums2[:n]
        add_list.sort()
        nums1[::] = add_list
        return nums1



s1 = Solution()
s2 = Solution2()

print(s1.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(s1.merge([1],1,[0],0))
print(s1.merge([],0,[1],1))
print(s1.merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3))


print(s2.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(s2.merge([1],1,[0],0))
print(s2.merge([],0,[1],1))
    





