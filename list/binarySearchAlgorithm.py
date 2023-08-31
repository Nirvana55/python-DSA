#Binary search algorithm is an algorithm which is used to find the element with the help of its two method 
#recursive and iterative method.

#It follows divide and conjure method.

#divide and conquer method is known for breaking the elements into sub elements and doing its task as it assigned.

#And the main thing is to do binary search list or elements should always be sorted.
#With that it will find the mid of the element by 
#arr[high+low /2]
#and if the number is greater than mid it will check by mid + 1
#else it will find by mid - 1

# recursive methods:
def binary_search(nums:list[int], target:int, low:int, high:int) -> int:
    if low <= high:
        mid_element = (low + high) //2
        if nums[mid_element] == target:
            return mid_element
        elif nums[mid_element] < target:
            return binary_search(nums,target,mid_element + 1,high)
        elif nums[mid_element] > target:
            return binary_search(nums,target,low,mid_element -1)
    else:
        return -1

result = binary_search([1,2,3,4,5,6],6, 1, 6)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

#Iterative method
def binary_search_2(nums:list[int],target:int,low:int,high:int):
    while low <= high:
        mid_element = (low + high) // 2
        if nums[mid_element] == target:
            return target
        elif nums[mid_element] > target:
            high = mid_element -1
        else:
            low = mid_element +1
    return -1
        
result2 = binary_search_2([1,2,3,4,5,6],6, 1, 6)

if result2 != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")