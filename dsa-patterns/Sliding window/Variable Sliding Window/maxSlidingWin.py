
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

    #easy to remember pseudocode for the above approach:
    # 1. Initialize an empty deque and an empty list for the output.
    # 2. Use two pointers, l and r, to represent the left and right edges of the sliding window.
    # 3. Iterate through the array with the right pointer r
    # 4. For each element nums[r], remove elements from the back of the deque if they are smaller than nums[r].
    # 5. Add the index r to the deque
    # 6. If the front of the deque is out of the current window (i.e., deq[0] < l), remove it from the front of the deque.
    # 7. If we have filled at least one window (i.e., r + 1 >= k), append the maximum element (nums[deq[0]]) to the output
    # 8. Move the left pointer l to the right to slide the window.      

        

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


   