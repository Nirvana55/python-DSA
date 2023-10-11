# Leet code level: Medium

# Question: Need to find the first and Last position of an element
# requirement is to find it on o(log(n))

# Break down:
# had to check the position of the element so we used the len(nums)
# to check the left most and not start from the right
# after finding the left most we check on the right most which is greater or equals to the target
# by doing this we later do subtraction of -1 so that we get the actual element
# later we check the low is less than or equal to high we return our output
# else return the error


class Solution:
    def searchRange(self, nums, target):
        def search(x):
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] < x:
                    low = mid + 1
                else:
                    high = mid
            return low

        low = search(target)
        high = search(target + 1) - 1

        if low <= high:
            return [low, high]

        return [-1, -1]


s1 = Solution()
print(s1.searchRange([5, 7, 7, 8, 8, 10], 8))
