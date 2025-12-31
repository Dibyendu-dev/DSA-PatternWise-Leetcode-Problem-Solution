class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_len = 0
        start = 0

        for end in range(len(s)):
            curr_char = s[end]
            if curr_char in char_index and char_index[curr_char] >= start:
                start = char_index[curr_char] + 1

            char_index[curr_char] = end
            curr_len = end - start + 1
            max_len = max(curr_len, max_len)

        return max_len
        
        