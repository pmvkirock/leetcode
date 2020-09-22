class Solution:
    def isPalindrome(self, s: str) -> bool:
        act_str = ''.join([e for e in s if e.isalnum()]).lower()
        
        start = 0
        last = len(act_str)-1
        
        while start < last:
            if act_str[start] != act_str[last]:
                return False
            start += 1
            last -= 1
        
        return True