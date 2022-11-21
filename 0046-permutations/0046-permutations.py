class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        #base case 
        if len(nums)==1:
            return [nums.copy()] #nums[:] deep copy
        
        for i in range(len(nums)):
            n = nums.pop(0) #popping 1 value and getting permutations of other values
            perms = self.permute(nums) #recursive call
            
            for perm in perms:
                perm.append(n)
            res.extend(perms) #extend for adding multiple values at a time
            nums.append(n) #appendin valu we have popped
            
        return res
            