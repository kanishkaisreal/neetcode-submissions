class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums)-1 

        while left <= right :
            mid  =  ( left+ right)//2 

# case 1 
            if nums[mid] == target:
                return mid 

# Case 2 :             
            # if the rotation is in the left
            elif nums[mid] >= nums[left]:
                # now we are sure in inside this loop that sorted list it on the left hand side 
                if target >=nums[left] and target < nums[mid]:
                    right = mid -1 
                else:
                    left = mid + 1 
            
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1 
                else :
                    right = mid -1 
        
        return -1 
