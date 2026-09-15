from git import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

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

#example usage
nums = [1,3,-1,-3,5,3,6,7]
k = 3
solution = Solution()
result = solution.maxSlidingWindow(nums, k)
print(f"The maximum values in each sliding window of size {k} are: {result}")   #output: The maximum values in each sliding window of size 3 are: [3, 3, 5, 5, 6, 7]