class Solution:
    def twoSum(self, nums, target):
        """
        Problem: Two Sum
        Description: Given an array of integers 'nums' and an integer 'target',
                     return indices of the two numbers such that they add up to target.
        Approach: Use a dictionary to store numbers already seen. For each number,
                  check if its complement (target - number) is in the dictionary.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # Dictionary to store numbers already seen and their indices
        seen = {}

        # Iterate through array
        for i, num in enumerate(nums):
            complement = target - num

            # If complement exists in dictionary, return indices
            if complement in seen:
                return [seen[complement], i]

            # Store current number with its index
            seen[num] = i

        # Return empty list if no solution found
        return []
