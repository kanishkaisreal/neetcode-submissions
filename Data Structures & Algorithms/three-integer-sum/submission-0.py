class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # first sort them out 
        n = len (nums)
        result = []

        
        for i in range(len(nums) - 2) : 
            # if current value is positive them it cannot add upto 0 
            if nums[i] > 0 :
                break
            
            # now skip the duplicates 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # now do the two pointers
            target = -nums[i] 
            left, right = i+1, n-1

            while left < right :
                total = nums[left] + nums[right] 

                if total > target:
                    right -=1 
                elif total < target:
                    left +=1 
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right-1]:
                        right -=1 
                    
                    left +=1 
                    right -= 1 
            
        return result 

        