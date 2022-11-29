class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        
        productBefore = productAfter = 1 #default at left and at right
        
        for i in range(len(nums)): #prev prodcut calculation
            ans[i] = productBefore
            productBefore = productBefore * nums[i]
            
        for i in range(len(nums)-1, -1, -1): #after product calculation for each point
            ans[i] = ans[i] * productAfter
            productAfter = productAfter * nums[i]
            
        return ans
            
            