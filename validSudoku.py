from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]  # Create a set for each row to track seen numbers
        #braking down the code in steps:


        cols = [set() for _ in range(9)]   # this will create a list of set for each column to track seen numbers
        boxes = [set() for _ in range(9)]    # this will create a set for each 3x3 sub-box to track seen numbers
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':  # Check if the cell is not empty
                    box_index = (r // 3) * 3 + (c // 3)

                    if (num in rows[r] or
                        num in cols[c] or
                        num in boxes[box_index]):
                        return False
                    #else continue
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

        return True
# Example usage:

solution = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", "6", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(solution.isValidSudoku(board))  # Output: True



#pseudocode :
# 1. Create a set to track seen numbers
# 2. Iterate through each row, column, and 3x3 sub-box
# 3. For each cell, if it contains a number, check if it has been seen before
# 4. If it has, return False
# 4. If not, add it to the set
# 5. If all checks pass, return True
# 6. Use a helper function to check the validity of each row, column, and sub-box --->
