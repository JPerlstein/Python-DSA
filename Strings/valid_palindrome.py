"""
Problem: Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Approach:
Use two pointers (left and right). Move pointers inward while skipping non-alphanumeric
characters. Compare characters; if any mismatch occurs, return False.

Time Complexity: O(n)
Space Complexity: O(1)
"""



class Solution:
    # returns - > boolean
    def isPalindrome(self, s: str) -> bool:
        # converting to lowercase 
        s = s.lower()

        # initializing left pointer 
        left = 0 

        # initializing right pointer 
        right = len(s) - 1 

        # while left is less than right 
        while left < right: 
            # if character on the left is not alphanumeric 
            if not s[left].isalnum(): 
                # move left pointer to the right 
                left += 1 
            # if character on the right is not alphanumeric      
            elif not s[right].isalnum():
                # move right pointer to the left 
                right -= 1     
            # if both characters (left and right) are alphanumeric 
            # and not equal 
            elif s[left] != s[right]:
                # return False because it is NOT a palindrome 
                return False 
            # otherwise
            # if both characters (left and right) are alphanumeric 
            else: 
                # move both pointers inward 
                left += 1 
                right -= 1 
        # if loop completes w/o returning
        # the input string IS a palindrome 
        # as such, function returns True         
        return True             
