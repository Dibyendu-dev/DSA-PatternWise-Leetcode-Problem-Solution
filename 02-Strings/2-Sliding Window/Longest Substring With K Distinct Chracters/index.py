class Solution:
    def longestSubstringWithAtMostKDistinctCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        char_count = {}
        start = 0
        max_lenth = 0

        for end in range(len(s)):
            char_count[s[end]] = char_count.get(s[end],0) +1

            while len(char_count) > k:
                char_count[s[start]] -=1
                if char_count[s[start]] == 0:
                    del char_count[s[start]]
                start +=1

            max_lenth = max(max_lenth,end-start+1)

        return max_lenth

