class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n 
# forward pass 
        prefix = 1 
        for i in range(n):
            output[i] = prefix 
            prefix *=nums[i]
        
          # Compute suffix on the fly while updating output 
        suffix = 1 
        for i in range(n-1, -1, -1):
            output[i] *= suffix   # this will be a on the fly update on the output, 
            # so you don't have to have two separate array suffix and prefix and then multuply them. 

            suffix *= nums[i]

        return output 

        