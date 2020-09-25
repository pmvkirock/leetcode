class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        maxlen = 0
        for i in s:
            if i in substr:
                if len(substr) > maxlen:
                    maxlen = len(substr)
                x = substr.find(i)
                substr = substr[x+1:]
            substr += i
                
        return max(len(substr),maxlen)