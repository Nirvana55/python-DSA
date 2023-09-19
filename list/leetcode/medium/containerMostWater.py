# leet code level: medium

# QUESTION: Container With Most Water

# Breakdown
# there will be given list
# we can set two pointers first and last
# we can check the min value of the pointer and width of the pointer by their indexes
# by calculating every index and finding the max value
# we can say that which container will have the max value


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0

        while left_pointer < right_pointer:
            current_area = min(height[left_pointer], height[right_pointer]) * (
                right_pointer - left_pointer
            )
            max_area = max(current_area, max_area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area


s1 = Solution()
print(s1.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
