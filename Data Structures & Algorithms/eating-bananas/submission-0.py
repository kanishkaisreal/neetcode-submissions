class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right  = 1, max(piles)

        while left < right :
            pivot = ( left + right ) // 2 

            hours = 0 

            for p in piles :
                hours += math.ceil(p/pivot)
            
            if hours <= h : # fast enough to try slow 
                right = pivot 
            else:    # hours > h 
                left = pivot + 1   
        return right 
        
        