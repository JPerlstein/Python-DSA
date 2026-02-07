class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Problem:
        Given an array `nums` containing `n` distinct numbers taken from the range
        [0, n], return the one number that is missing from the array.

        Example:
        Input: nums = [3, 0, 1]
        Output: 2

        Approach:
        - The numbers should ideally include every value from 0 to n exactly once.
        - Instead of computing the expected sum using a formula, we use a
          running balance technique.
        - We start with `n` (the length of the array).
        - For each index `i`, we:
            * add the index `i`
            * subtract the value `nums[i]`
        - All numbers that exist cancel out, leaving only the missing number.

        Why this works:
        - Indices generate the sequence 0 through n-1.
        - Starting with n accounts for the final number in the range.
        - Since every number except one appears exactly once, everything cancels
          out except the missing value.

        Time Complexity:
        O(n) — iterate through the list once.

        Space Complexity:
        O(1) — used only a single variable for computation.
        """

        # storing length of input list 
        n = len(nums)

        # initializing result with n to account for the full range [0, n]
        result = n

        # iterate over each index in the list
        for i in range(n):
            # add index and subtract corresponding value
            # causes existing numbers to cancel out
            result += i - nums[i]

        # remaining value is the missing number
        return result
