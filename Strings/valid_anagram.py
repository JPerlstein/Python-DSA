#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Problem:
        Given two strings s and t, return true if t is an anagram of s, 
        and false otherwise. An anagram is a word formed by rearranging 
        the letters of a different word, typically using all the original 
        letters exactly once.

        Example:
        Input: s = "anagram", t = "nagaram" -> Output: True
        Input: s = "rat", t = "car"         -> Output: False

        Approach:
        1. Check if the lengths of both strings are equal; if not, return False.
        2. Use two hash maps (dictionaries) to store the frequency of each 
           character in both strings.
        3. Iterate through both strings simultaneously to populate the maps.
        4. Compare the two maps; if they are identical, the strings are anagrams.

        Complexity:
        - Time Complexity: O(n), where n is the length of the strings. 
          We iterate through the strings once.
        - Space Complexity: O(k), where k is the number of unique characters. 
          If the character set is fixed (e.g., 26 lowercase letters), this is O(1).
        """
        
        # if the length of s and t are NOT equal, they cannot be anagrams
        if len(s) != len(t):
            return False

        # creating empty dictionaries to store character counts
        # for string s and string t 
        s_dict = {}
        t_dict = {}

        # looping through each index i of the strings
        for i in range(len(s)):
            # incrementing the count of the character s[i] in s_dict
            # if s[i] is not yet in s_dict, get() returns 0, then add 1
            # updating the count
            # counting how many times a char appears in s string 
            # then stores it in the dict 
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1

            # incrementing the count of the character t[i] in t_dict
            # if t[i] is not yet in t_dict, get() returns 0, then add 1
            # updating the count
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        # compare both dictionaries, if they are equal, s and t ARE anagrams
        return s_dict == t_dict   

