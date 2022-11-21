class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        
        def dfs_backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n] >0 :
                    perm.append(n)
                    count[n] -= 1
                    dfs_backtrack()
                    
                    #cleaning up
                    perm.pop()
                    count[n] += 1
        
        dfs_backtrack()
        return res
                    
            