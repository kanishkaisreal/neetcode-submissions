class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned =  ''.join(c.lower() for c in s if c.isalnum())

        # use two pointer approach. 

        left, right  = 0 , len(cleaned) - 1 
        while left < right :
            if cleaned[left] == cleaned[right] : 
                left +=1 
                right -= 1 
            else:
                return False
        
        return True 
        



        