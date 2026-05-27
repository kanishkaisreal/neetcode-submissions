class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0 
        maxlength = 0 
        charset = set()

        while right  <  len(s):
            while s[right] in charset : 
                charset.remove(s[left])
                left += 1
            
            charset.add(s[right])
            
            maxlength=  max(maxlength, right - left + 1 ) 
            right += 1 
        
        return maxlength 



        