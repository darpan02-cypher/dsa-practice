from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {} # a dictionary to store the frequency of each element
        # iterate through the list and count the frequency of each element
        # if the element is not in the dictionary, initialize it with an empty list
        # and increment the count
        # if the element is already in the dictionary, increment the count
        # finally, return the top k frequent elements
        count=0
        for i in nums:            
            if i not in res:
                res[i]=[] #initialize with empty list
                count=count+1; #frequency
            res[i]= count #append the frequency as value in dictionary
        return list(sorted(res.keys(), reverse=True)[:k]) # sort the keys in descending order and return the top k frequent elements
        

solution=Solution()
nums = [1,2,2,3,3,3]
k = 2
print(solution.topKFrequent(nums, k))


        