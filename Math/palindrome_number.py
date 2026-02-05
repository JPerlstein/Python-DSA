"""
Problem: Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.
A palindrome is a number that reads the same forward and backward.

Approach:
Convert the integer to a string, then reverse the string using slicing.
If the reversed string is equal to the original string, the number is a palindrome.

Time Complexity: O(n)
Space Complexity: O(n)
"""



class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert the integer to a string
        convert_to_string = str(x)

        # reverse the string using slice notation [::-1]
        # the -1 means iterating through the string backwards
        # return True if the string is the same forwards and backwards
        return convert_to_string == convert_to_string[::-1]
