#leet code level: Easy

#Question: Given an integer n, return a string array answer:

#Algorithm:
#step1: loop with the int:
#step2: convert the list element into number and implement divide
#step3: set variable value according to it
#step4: return list

# Time complexity 0(n) and spaceComplexity 0(n)
class Solution:
    def fizzBuzz(self, n: int) -> list[str]: 
        answer = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                answer.append("FizzBuzz")
            elif i%3 == 0:
                answer.append("Fizz")
            elif i%5 ==0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

s1 = Solution()
print(s1.fizzBuzz(16))
