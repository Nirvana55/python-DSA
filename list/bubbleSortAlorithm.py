#Topic: Bubble sort algorithm

#Bubble sort algorithm is one of the popular algorithm for sorting an input.
#It states that when we loop and compare largest with all element it will sort the last element on right.
#with same flow we can find the largest element

#Algorithm:
#step1: loop first with i
#step2: loop second but need to decrease the range cause last element is already sorted
#step3: swap the element
#step4: end

#Extra: we can use list.sort() now which is optimized
#cause this is bad for time complexity

class BubbleSortAlgorithm:
    def sort_list(self,nums:list[int])-> list:
        for i in range(len(nums)):
            # decreasing here to match the index
            for j in range(0, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j],nums[j+1]
        return nums
    
s1 = BubbleSortAlgorithm()
print(s1.sort_list([2,4,5,6,2,1]))




