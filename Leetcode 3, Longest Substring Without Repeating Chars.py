# Leetcode Problem 3, Longest Substring Without Repeating Chars

"""Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""

# This problem uses Sliding Window Algorithm as a basis

# Must learn this algorithm as many similar problems use this concept

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()

        left_pointer = 0
        right_pointer = 0
        longest_Substring = 0

        for right_pointer in range( len(s) ):   #range is from 0 - length of s
            while s[right_pointer] in char_set:
                char_set.remove( s[left_pointer] )
                left_pointer += 1
            char_set.add( s[right_pointer] )
            longest_Substring = max( longest_Substring, right_pointer - left_pointer + 1 ) #right_pointer - left_pointer + 1 is the length of our current substring
        return longest_Substring