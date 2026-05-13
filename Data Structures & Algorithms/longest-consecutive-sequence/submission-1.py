class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the idea here is that we see every number and check if it has a left neighbour. 
        #numbers that have left neighbour are not start of sequence.. 
        # numbers that have NO left neightbour are start of sequence 
    # a sequence that we mesure to start measuring lenght only for that for which the left neighbout don't exist. 
        nums_set = set(nums)
        longest_streak = 0 
        for num in nums_set:
            if num -1 not in nums_set:  # check if it is start of the new sequence ( mening left neightbour don't exist , and since left enightbour don't exist, it is start of the sequence ) 
                current_num  = num 
                current_streak = 1 
                
                while current_num +1 in nums_set:
                    current_num +=1 
                    current_streak +=1 
                
                longest_streak = max(longest_streak, current_streak)
            
        return longest_streak

        