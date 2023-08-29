#leet code level: Easy 

#Question: need to increase the size of the list with one 
#example: [9] : [1,0] = 10

#Algorithm:
#need to convert into a str and later to int
#and add and covert it to list

#time complexity: 0(n)
#spaceComplexity:0(n)
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        string = ""
        for i in digits:
            string += str(i)
        
        temp = str(int(string) + 1)
        return [int(i) for i in temp]

#time complexity: 0(n)
#spaceComplexity: 0(n)   
class Solution2:
    def plusOne(self, digits: list[int]) -> list[int]:
        # we are starting from the right most
        # we are decreased the length of list and checked the last value
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

    
s1 = Solution()
s2 = Solution()

print(s1.plusOne([1,2,3]))
print(s2.plusOne([1,2,3]))