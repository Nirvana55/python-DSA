#Leet code level: easy

#Question: need to find the majority of the list

# Boyer-More majority Algorithm:
#-> description:
# If there are a voting candidate. Bunch of people are voting them. If the first element the vote should always be 1 to that candidate.
# When voting if same candidate we can add vote by 1.
# Else we can decrease the vote.
# after that we check the vote from the bucket. 
# we total the vote and make it it total.
# To find the majority if the total vote is greater than half of the people. It is already the winner.
# So this is what he stated example in a simple way.

#algorithm: 
#Step1: variable assign vote -> 0, the candidate -> -1, total_vote_count -> 1
#step2: loop the list 
#step3: if the first character set vote as 1 and assign candidate
#step4: if current element is equal to prev element add else decrease count.
#step5: loop again and compare candidate on list, increase the count of the vote
#step6: compare the total_vote_count with half of list.
#step7: end


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        vote = 0
        candidate = -1
        total_vote_count = 0
        for i in range(len(nums)):
            if vote == 0:
                candidate = nums[i]
                vote = 1
            elif nums[i] == candidate:
                vote += 1
            else:
                vote -= 1

        # We could have returned candidate here directly but we just followed
        # Boyer-More Algorithm
        for i in range(len(nums)):
            if (nums[i] == candidate):
                total_vote_count+=1
        
        if (len(nums)/2) < total_vote_count:
            return candidate
       
        

s1 = Solution()
print(s1.majorityElement([1,2,4,4,4,4,4,4,5]))
print(s1.majorityElement([1,2,2,2]))