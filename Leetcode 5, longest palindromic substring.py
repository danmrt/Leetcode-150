class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        
        s_left = 0
        s_right = 0
        longest_string_count = 0
        longest_s_right = 0
        longest_s_left = 0

        #odd
        for i in range( 0,len(s) ):
            s_left = i
            s_right = i

            while s_left >= 0 and s_right < len(s) and s[s_left] == s[s_right]:
                longest_string_count = max( longest_string_count, s_right - s_left + 1 )
                if longest_string_count == (s_right - s_left + 1):
                    longest_s_left = s_left
                    longest_s_right = s_right
                s_left = s_left - 1
                s_right = s_right + 1

        palindrome_substring_odd = s[ longest_s_left: longest_s_right + 1]

        #even
        longest_s_left = 0
        longest_s_right = 1
        longest_string_count = 0

        for i in range( 0, len(s) ):
            s_left = i
            s_right = i + 1
            while s_left >= 0 and s_right < len(s) and s[s_left] == s[s_right]:
                longest_string_count = max( longest_string_count, s_right - s_left + 1 )
                if longest_string_count == (s_right - s_left + 1):
                    longest_s_left = s_left
                    longest_s_right = s_right
                s_left = s_left - 1
                s_right = s_right + 1
        
        if s[longest_s_left] == s[longest_s_right]:
            palindrome_substring_even = s[ longest_s_left: longest_s_right + 1]
        else:
            palindrome_substring_even = ""

        ultimate_longest_string = max(palindrome_substring_odd, palindrome_substring_even,key = len)

        return ultimate_longest_string


        