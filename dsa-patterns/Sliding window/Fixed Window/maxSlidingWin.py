
from git import List
from collections import deque



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

         #Optimized approach using Deque - O(n) time complexity
                output = []
                deq = deque() #storing the index of the elements in the current window
                l=r=0 #pointers start at the beginning of the array
        
                while r < len(nums):
                    #remove elements from the back of the deque if they are smaller than the current element
                    while deq and nums[deq[-1]] < nums[r]:
                        deq.pop()
        
                    #add the current element's index to the deque
                    deq.append(r)
        
                    #remove the front element if it is out of the current window
                    if deq[0] < l:
                        deq.popleft()
        
                    #if we have filled at least one window, add the maximum to the output
                    if r + 1 >= k:
                        output.append(nums[deq[0]])
                        l += 1
        
                    r += 1
                return output
        

'''
        #brute force
        #Below approac has O(n*k) time complexity - very high ..not suits leetcode
        res= [] #array to store final result

        #win_max= max(nums[:k]) #initial set to first window max
        #l = nums[0]

        for i in range(len(nums) - k + 1):
            #win_max = max(nums[i], nums[i+1], nums[i+k-1])
            r=i+k
            l=i
            win_max = max(nums[l:r])
            res.append(win_max)
        return res
    #the time complexity of the above approach is very high (not suits leetcode-gives error there) - O(n*k) where n is the length of the input array and k is the size of the sliding window. This is because for each of the n-k+1 windows, we are calculating the maximum value in O(k) time.
'''
#example usage
nums = [1,3,-1,-3,5,3,6,7]
k = 3
solution = Solution()
result = solution.maxSlidingWindow(nums, k)
print(f"The maximum values in each sliding window of size {k} are: {result}")   #output: The maximum values in each sliding window of size 3 are: [3, 3, 5, 5, 6, 7]


   