#leet code level: easy

#Question: need to find the longest prefix of the list

# Breakdown:
# there will be string in list
# need to sort the string into lexicographic
# need to compare the minimum value between two string
# need to compare the value of the first and string
# if not equal return string
# else return the string
# end

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        new_list = sorted(strs)
        first_string = new_list[0]
        last_string = new_list[-1]
        for i in range(len(min(first_string,last_string))):
            if first_string[i] != last_string[i]:
                return ans
            ans += first_string[i]
        return ans

s1 = Solution()
print(s1.longestCommonPrefix(["flower","flow","flight"]))

