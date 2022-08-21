# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t) # dict of unique char in t
        unique = len(dict_t) # number of unique char in t
        left = 0
        right = 0
        formed = 0 # how many conditions formed
        window_counts = {} # dict of unique char in current window
        res = float("inf"), None, None # tuple

        while right < len(s):
            character = s[right] # Add 1 character from right to the window
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while left <= right and formed == unique:
                character = s[left]

                if right - left + 1 < res[0]: # Save the smallest window until now.
                    res = (right - left + 1, left, right)

                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                left += 1    
            right += 1    
        return "" if res[0] == float("inf") else s[res[1] : res[2] + 1]