from typing import List


class Solution:

    
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(heights[left], heights[right]) * width
            max_area = max(max_area, current_area)

            if heights[left] <= heights[right]: 
                left += 1 #If the new height at right-1 is taller, the container height is still capped at heights[left].
                        #If the new height at right-1 is shorter, the container height becomes even smaller

            else:
                right -= 1 #If the new height at left+1 is taller, the container height is still capped at heights[right].
                        #If the new height at left+1 is shorter, the container height becomes even smaller

        return max_area

#example usage
solution = Solution()
heights = [1,7,2,5,4,7,3,6]
result = solution.maxArea(heights)
print(result)  # Output: 36