from typing import List


def removeElement(nums: List[int], target: int):
    # k acts as the pointer for valid elements (count of non-target items)
    k = 0

    for i in range(len(nums)):
        if nums[i] != target:
            nums[k] = nums[i]
            k += 1

    return nums, k


# ---------------------------------------------------------
# Test Cases & Example Usage
# ---------------------------------------------------------

tests = [
    ([3, 2, 2, 3], 3, 2, [2, 2]),  # Mixed elements
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),  # Multiple duplicates
    ([], 1, 0, []),  # Empty array
    ([1, 2, 3, 4], 5, 4, [1, 2, 3, 4]),  # Target not in array
    ([2, 2, 2], 2, 0, []),  # All elements match target
    ([1], 1, 0, []),  # Single element (matches)
    ([1], 2, 1, [1]),  # Single element (does not match)
]

for nums, target, expected_k, expected_nums in tests:
    arr = nums.copy()
    modified_arr, k = removeElement(arr, target)

    passed = k == expected_k and sorted(modified_arr[:k]) == sorted(expected_nums)
    status = "PASS" if passed else "FAIL"

    print(f"[{status}] target={target} | original={nums} -> k={k}, modified={modified_arr[:k]}")

