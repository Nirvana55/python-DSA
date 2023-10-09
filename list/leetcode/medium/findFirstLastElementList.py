# Leet code level: Medium

# Question: Need to find the first and Last position of an element
# requirement is to find it on o(log(n))


class Solution:
    def searchRange(self, nums, target):
        def search(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        lo = search(target)
        hi = search(target + 1) - 1

        if lo <= hi:
            return [lo, hi]

        return [-1, -1]


s1 = Solution()
print(s1.searchRange([5, 7, 7, 8, 8, 10], 8))
